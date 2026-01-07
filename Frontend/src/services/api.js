const API_BASE_URL = "http://127.0.0.1:8000";

export async function processLecture(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_BASE_URL}/process-lecture`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Failed to process lecture");
  }

  return await response.json();
}
