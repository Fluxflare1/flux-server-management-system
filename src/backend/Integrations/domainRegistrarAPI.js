const axios = require('axios');

async function registerDomain(domainName) {
    try {
        const response = await axios.post('https://domain-registrar.example.com/register', { domainName });
        console.log("Domain registered successfully:", response.data);
    } catch (error) {
        console.error("Domain registration failed:", error);
    }
}

module.exports = { registerDomain };
