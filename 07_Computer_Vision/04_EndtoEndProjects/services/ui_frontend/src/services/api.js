const API_BASE = 'http://localhost:9000/api';

export async function fetchViolations() {
  const res = await fetch(`${API_BASE}/violations`);
  if (!res.ok) throw new Error("Failed to fetch violations");
  return res.json();
}

