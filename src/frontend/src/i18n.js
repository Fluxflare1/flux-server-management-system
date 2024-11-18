// Path: frontend/src/i18n.js
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';

const resources = {
  en: {
    translation: {
      "Welcome": "Welcome",
      "Dashboard": "Dashboard",
    },
  },
  es: {
    translation: {
      "Welcome": "Bienvenido",
      "Dashboard": "Tablero",
    },
  },
};

i18n.use(initReactI18next).init({
  resources,
  lng: "en",
  interpolation: { escapeValue: false },
});

export default i18n;
