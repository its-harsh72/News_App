const fetch = require('node-fetch');
const fs = require('fs');
const { PDFDocument } = require('pdf-lib');

async function extractTextFromPDF(url) {
    const response = await fetch(url);
    const pdfBytes = await response.arrayBuffer();

    fs.writeFileSync('downloaded_pdf.pdf', Buffer.from(pdfBytes));

    const pdfDoc = await PDFDocument.load(pdfBytes);
    const text = [];
    for (let i = 0; i < pdfDoc.getPageCount(); i++) {
        const page = pdfDoc.getPage(i + 1);
        const content = await page.getTextContent();
        const pageText = content.items.map(item => item.str).join('');
        text.push(pageText);
    }
    return text.join('\n');
}

const pdfUrl = "https://myamo.amoga.io/non_prod/credable/2024/5/15/tooljet/CAN-YANTRALIVE_PARTS_TECHNOLOGY_PRIVATE_LIMITED_280224_HCwATGJ.pdf";
extractTextFromPDF(pdfUrl)
    .then(text => console.log(text))
    .catch(error => console.error(error));

    