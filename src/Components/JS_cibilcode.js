const axios = require('axios');
const fs = require('fs');
const { PDFDocument } = require('pdf-lib');
const { dialog } = require('electron');

async function extractTextFromPDF(url) {
    const response = await axios.get(url, { responseType: 'arraybuffer' });
    const dataBuffer = Buffer.from(response.data);

    const pdfDoc = await PDFDocument.load(dataBuffer);
    const textContent = await pdfDoc.getText();

    return textContent;
}

function extractCompanyNameAndRank(text) {
    let companyName = null;
    let rank = null;
    const searchCriteriaMatch = text.match(/Search Criteria:\s*(.*?),/);
    if (searchCriteriaMatch) {
        companyName = searchCriteriaMatch[1].trim();
    }

    const rankMatch = text.match(/Rank\s+(\w+-\d+)/);
    if (rankMatch) {
        rank = rankMatch[1];
    }

    return { companyName, rank };
}

function findNumericValuesAndAmounts(text) {
    return text.matchAll(/(Total\s*-\s*#\d+)\s*₹([\d,]+)/g);
}

function printMaxNumericValueAndAmount(numericValuesAndAmounts) {
    if (!numericValuesAndAmounts) return ["No numeric values found.", null];

    let max = { value: -Infinity, amount: null };

    for (const match of numericValuesAndAmounts) {
        const value = parseInt(match[1].split('#')[1]);
        if (value > max.value) {
            max.value = value;
            max.amount = "₹" + match[2];
        }
    }

    return [`#${max.value}`, max.amount];
}

function findTotalAfterEnquirySummary(text) {
    const match = text.match(/5\. Enquiry Summary.*?Total\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)/s);
    if (!match) return null;

    const totalValues = match.slice(1).map(value => parseInt(value)).filter(value => !isNaN(value));
    return totalValues.reduce((acc, cur) => acc + cur, 0);
}

function findNonZeroOverdue(text) {
    const pattern = /Overdue:\s*(?!0(?:\.0+)?$)(\d+(?:\.\d+)?)/g;
    const matches = text.match(pattern);

    if (!matches) return ["No 'Overdue:' values found.", null];

    const nonZeroOverdueValues = matches.map(match => parseFloat(match)).filter(value => value !== 0);
    if (!nonZeroOverdueValues.length) return ["No Overdue.", null];

    const latestDpd = findLatestDpd(text);
    return [nonZeroOverdueValues, latestDpd];
}

function findLatestDpd(text) {
    const matches = text.match(/[01] DPD/g) || [];
    return matches.length ? matches[matches.length - 1] : "No DPD found";
}

async function generateCSV() {
    const pdfUrl = "https://myamo.amoga.io/non_prod/credable/2024/5/17/tooljet/GIFTS_PLANET_PRIVATE_LIMITED_CIBIL_3Evbvtl.pdf";
    const text = await extractTextFromPDF(pdfUrl);

    const { companyName, rank } = extractCompanyNameAndRank(text);
    const numericValuesAndAmounts = [...findNumericValuesAndAmounts(text)];
    const [maxValue, associatedAmount] = printMaxNumericValueAndAmount(numericValuesAndAmounts);
    const totalValue = findTotalAfterEnquirySummary(text);
    const [overdueValues, latestDpd] = findNonZeroOverdue(text);

    const result = await dialog.showSaveDialog({
        defaultPath: "output.csv",
        filters: [{ name: 'CSV files', extensions: ['csv'] }]
    });

    if (result.canceled) {
        console.log("File save was canceled");
        return;
    }

    const filePath = result.filePath;

    const rows = [
        ["Company Name", "Rank", "Max Value", "Associated Amount (₹)", "Enquiry Summary", "Overdue", "Latest DPD"],
        [companyName, rank, maxValue, associatedAmount, totalValue, overdueValues.join(','), latestDpd]
    ];

    const csvContent = rows.map(row => row.join(',')).join('\n');
    fs.writeFileSync(filePath, csvContent);

    console.log("CSV file generated successfully at:", filePath);
}

generateCSV();
