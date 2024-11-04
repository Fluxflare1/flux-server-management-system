// src/backend/automation/AccountTerminationScheduler.js
const cron = require('node-cron');
const AutomationManager = require('./AutomationManager');

class AccountTerminationScheduler {
    static initializeAutomationTasks() {
        // Daily check for overdue accounts to suspend
        cron.schedule('0 0 * * *', () => {
            AutomationManager.suspendOverdueAccounts();
        });
        
        // Weekly check for inactive accounts to terminate
        cron.schedule('0 0 * * 0', () => {
            AutomationManager.terminateInactiveAccounts();
        });
        
        console.log('Automation tasks scheduled.');
    }
}

module.exports = AccountTerminationScheduler;
