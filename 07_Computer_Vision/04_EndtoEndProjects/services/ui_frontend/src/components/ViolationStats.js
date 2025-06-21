import React, { useEffect, useState } from 'react';
import { fetchViolations } from '../services/api';

const ViolationStats = () => {
  const [violations, setViolations] = useState(0);

  useEffect(() => {
    const interval = setInterval(async () => {
      try {
        const data = await fetchViolations();
        setViolations(data.total_violations);
      } catch (err) {
        console.error(err);
      }
    }, 3000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h2>Violations Detected: {violations}</h2>
    </div>
  );
};

export default ViolationStats;

