const API_BASE_URL = "https://ashwin-sangokar-lecture-voice-to-notes-backend.hf.space";

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
