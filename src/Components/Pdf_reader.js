const axios = require('axios');
const fs = require('fs');
const { PDFDocument } = require('pdf-lib');

// URL of the PDF you want to read
const pdfUrl = 'https://myamo.amoga.io/non_prod/credable/2024/5/17/tooljet/GIFTS_PLANET_PRIVATE_LIMITED_CIBIL_3Evbvtl.pdf';

// Function to download PDF from URL
async function downloadPDF(url) {
    const response = await axios.get(url, { responseType: 'arraybuffer' });
    return response.data;
}

// Asynchronous function to read the PDF
async function readPDF(url) {
    try {
        // Download the PDF
        const pdfBuffer = await downloadPDF(url);

        // Load PDF into PDFDocument object
        const pdfDoc = await PDFDocument.load(pdfBuffer);

        // Get the total number of pages in the PDF
        const numPages = pdfDoc.getPageCount();

        // Loop through each page and extract the text content
        for (let i = 0; i < numPages; i++) {
            const page = pdfDoc.getPage(i);
            const text = await page.getTextContent();
            console.log(`Text content of page ${i + 1}:`, text);
        }
    } catch (error) {
        console.error('Error reading PDF:', error);
    }
}

// Call the function to read the PDF
readPDF(pdfUrl);
