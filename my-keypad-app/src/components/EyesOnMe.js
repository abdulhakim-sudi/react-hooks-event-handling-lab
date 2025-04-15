// components/EyesOnMe.js

import React from 'react';

function EyesOnMe() {
  // Event handler for the focus event
  const handleFocus = () => {
    console.log('Good!');
  };

  // Event handler for the blur event
  const handleBlur = () => {
    console.log('Hey! Eyes on me!');
  };

  return (
    <div>
      <button 
        onFocus={handleFocus} 
        onBlur={handleBlur}
      >
        Eyes on me
      </button>
    </div>
  );
}

export default EyesOnMe;
