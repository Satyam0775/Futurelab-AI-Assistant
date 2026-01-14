import { useEffect, useRef, useState } from "react";

export default function App() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      text: "Hello. I'm the Futurelab AI Assistant. How can I help you today?",
      time: new Date().toLocaleTimeString()
    }
  ]);

  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef(null);

  // ✅ Scroll to bottom on new messages
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, loading]);

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim() || loading) return;

    const userMessage = {
      role: "user",
      text: input,
      time: new Date().toLocaleTimeString()
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      // ✅ ENV VARIABLE (WORKS ON VERCEL)
      const API_URL = import.meta.env.VITE_API_URL;

      if (!API_URL) {
        throw new Error("API URL not configured");
      }

      const response = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: userMessage.text })
      });

      if (!response.ok) {
        throw new Error("Backend error");
      }

      const data = await response.json();

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: data.reply,
          time: new Date().toLocaleTimeString()
        }
      ]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text:
            "Sorry, something went wrong while processing your request. Please try again.",
          time: new Date().toLocaleTimeString()
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-root">
      <aside className="sidebar">
        <h2>Futurelab</h2>
        <p>AI Assistant</p>
      </aside>

      <main className="chat-panel">
        <header className="chat-header">
          <span>Status: Online</span>
        </header>

        <section className="chat-messages">
          {messages.map((msg, index) => (
            <div key={index} className={`msg ${msg.role}`}>
              <div className="bubble">{msg.text}</div>
              <div className="time">{msg.time}</div>
            </div>
          ))}

          {loading && (
            <div className="msg assistant">
              <div className="bubble typing">AI is typing…</div>
            </div>
          )}

          <div ref={bottomRef} />
        </section>

        <form className="chat-input" onSubmit={sendMessage}>
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message…"
          />
          <button type="submit" disabled={loading}>
            Send
          </button>
        </form>
      </main>
    </div>
  );
}
