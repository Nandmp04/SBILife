export default function handler(req, res) {
  if (req.method === "POST") {
    const { savings, goal, scheme } = req.body;

    // Simple dummy logic
    let color = "red";
    if (savings > 500000) color = "green";
    else if (savings > 250000) color = "orange";

    res.status(200).json({
      color,
      suggestion: `For your goal: ${goal} and scheme: ${scheme}, this is a ${color.toUpperCase()} signal.`,
    });
  } else {
    res.status(405).json({ message: "Method Not Allowed" });
  }
}
