// Path: frontend/src/components/Onboarding/SetupWizard.js
import React, { useState } from 'react';

const SetupWizard = ({ onComplete }) => {
  const [step, setStep] = useState(1);

  const handleNext = () => {
    if (step < 3) setStep(step + 1);
    else onComplete();
  };

  return (
    <div>
      {step === 1 && <p>Step 1: Add your first server.</p>}
      {step === 2 && <p>Step 2: Configure your billing preferences.</p>}
      {step === 3 && <p>Step 3: Set up notifications.</p>}
      <button onClick={handleNext}>{step < 3 ? 'Next' : 'Finish'}</button>
    </div>
  );
};

export default SetupWizard;
