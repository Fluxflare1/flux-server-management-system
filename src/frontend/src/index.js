

import * as Sentry from "@sentry/react";
import { Integrations } from "@sentry/tracing";

Sentry.init({
    dsn: "https://<your-sentry-dsn>",
    integrations: [new Integrations.BrowserTracing()],
    tracesSampleRate: 1.0,
});



import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import * as serviceWorker from './serviceWorker';

ReactDOM.render(<App />, document.getElementById('root'));

// Register service worker for offline support
serviceWorker.register();
