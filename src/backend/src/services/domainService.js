// backend/src/services/domainService.js
const axios = require('axios');

// Register a domain
const registerDomain = async (domainName) => {
    const response = await axios.post('https://domain-registrar-api/register', { domain: domainName });
    return response.data;
};

// Renew a domain
const renewDomain = async (domainName) => {
    const response = await axios.post('https://domain-registrar-api/renew', { domain: domainName });
    return response.data;
};

module.exports = { registerDomain, renewDomain };
