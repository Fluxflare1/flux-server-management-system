// src/backend/reports/ReportScheduler.js
const cron = require('node-cron');
const AdvancedReportsGenerator = require('./AdvancedReportsGenerator');
const emailService = require('../services/emailService');

class ReportScheduler {
    static scheduleReportDelivery() {
        // Schedule weekly reports every Monday at 9 AM
        cron.schedule('0 9 * * 1', async () => {
            const insights = await AdvancedReportsGenerator.generateUsageInsightsReport();
            
            // Email the report to administrators
            await emailService.send({
                to: 'admin@yourdomain.com',
                subject: 'Weekly Usage Insights Report',
                body: 'Attached is the latest usage insights report.',
                attachments: [{ filename: 'UsageInsightsReport.json', content: JSON.stringify(insights) }]
            });
            console.log('Weekly Usage Insights Report emailed to administrators');
        });
    }
}

module.exports = ReportScheduler;
