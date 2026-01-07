function Results({ data }) {
  return (
    <div className="mt-6 space-y-6">
      {/* Summary */}
      <section>
        <h3 className="text-lg font-semibold mb-2">Summary</h3>
        <p className="bg-blue-50 p-4 rounded">
          {data.summary}
        </p>
      </section>

      {/* Key Points */}
      <section>
        <h3 className="text-lg font-semibold mb-2">Key Points</h3>
        <ul className="list-disc list-inside bg-gray-50 p-4 rounded">
          {data.key_points.map((point, index) => (
            <li key={index}>{point}</li>
          ))}
        </ul>
      </section>

      {/* Quiz */}
      <section>
        <h3 className="text-lg font-semibold mb-2">Quiz Questions</h3>
        <ol className="list-decimal list-inside bg-gray-50 p-4 rounded">
          {data.quiz.map((q, index) => (
            <li key={index}>{q}</li>
          ))}
        </ol>
      </section>

      {/* Transcript */}
      <section>
        <h3 className="text-lg font-semibold mb-2">Full Transcript</h3>
        <div className="bg-gray-100 p-4 rounded max-h-64 overflow-auto text-sm">
          {data.transcript}
        </div>
      </section>
    </div>
  );
}

export default Results;
