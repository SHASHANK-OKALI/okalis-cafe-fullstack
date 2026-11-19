const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000/api").replace(/\/$/, "");

export async function apiRequest(endpoint, options = {}) {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    headers: { "Content-Type": "application/json", ...(options.headers || {}) },
  });
  const payload = await response.json().catch(() => ({}));
  if (!response.ok) {
    const message = Object.entries(payload).map(([field, value]) => `${field}: ${Array.isArray(value) ? value.join(" ") : typeof value === "string" ? value : JSON.stringify(value)}`).join("\n") || `Request failed (${response.status})`;
    throw new Error(message);
  }
  return payload;
}

export { API_BASE_URL };
