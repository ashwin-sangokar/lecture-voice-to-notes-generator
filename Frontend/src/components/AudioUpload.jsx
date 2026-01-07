import Results from "./Results";
import { useState } from "react";
import { processLecture } from "../services/api";

function AudioUpload() {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setResult(null);
    setError(null);
  };

  const handleSubmit = async () => {
    if (!file) {
      alert("Please select an audio file first");
      return;
    }

    try {
      setLoading(true);
      const data = await processLecture(file);
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-md w-full max-w-2xl">
      <h2 className="text-xl font-semibold mb-4">
        Upload Lecture Audio
      </h2>

      <input
        type="file"
        accept="audio/*"
        onChange={handleFileChange}
        className="mb-4"
      />

      {file && (
        <p className="text-sm text-gray-600 mb-4">
          Selected: {file.name}
        </p>
      )}

      <button
  onClick={handleSubmit}
  disabled={loading || !file}
  className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700 disabled:opacity-50"
>
  {loading ? "Processing..." : "Process Lecture"}
</button>


      {error && (
  <div className="mt-4 bg-red-50 border border-red-300 text-red-700 p-3 rounded">
    {error}
  </div>
)}


      {result && <Results data={result} />}

    </div>
  );
}

export default AudioUpload;
