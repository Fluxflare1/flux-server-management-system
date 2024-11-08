const { registerDomain } = require('../integrations/domainRegistrarAPI');

async function automateDomainRegistration(domainName) {
    await registerDomain(domainName);
}

module.exports = { automateDomainRegistration };
