// OnboardingWizard.js - React component for onboarding wizard

import React, { useState } from 'react';

function OnboardingWizard() {
  const [step, setStep] = useState(1);

  const handleNext = () => setStep(step + 1);
  const handlePrevious = () => setStep(step - 1);

  return (
    <div>
      {step === 1 && <ProjectSetup />}
      {step === 2 && <EnvironmentSelection />}
      <button onClick={handlePrevious} disabled={step === 1}>Previous</button>
      <button onClick={handleNext}>Next</button>
    </div>
  );
}

export default OnboardingWizard;
