// src/backend/automation/AutomationManager.js
const db = require('../config/database');

class AutomationManager {
    static async suspendOverdueAccounts() {
        const overdueAccounts = await db.query('SELECT * FROM accounts WHERE status = "active" AND overdue = TRUE');
        
        overdueAccounts.forEach(async (account) => {
            await db.query('UPDATE accounts SET status = "suspended" WHERE id = ?', [account.id]);
            console.log(`Suspended account with ID: ${account.id}`);
        });
    }

    static async terminateInactiveAccounts() {
        const inactiveAccounts = await db.query('SELECT * FROM accounts WHERE status = "suspended" AND last_active < DATE_SUB(NOW(), INTERVAL 30 DAY)');
        
        inactiveAccounts.forEach(async (account) => {
            await db.query('DELETE FROM accounts WHERE id = ?', [account.id]);
            console.log(`Terminated account with ID: ${account.id}`);
        });
    }
}

module.exports = AutomationManager;
