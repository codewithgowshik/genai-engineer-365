import React, { useState } from "react";
import "./App.css"; 

export default function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  async function sendMessage(e) {
    e.preventDefault();

    const question = input.trim();
    if (!question || loading) return;

    setMessages((prev) => [
      ...prev,
      { role: "user", content: question },
      { role: "assistant", content: "" },
    ]);

    setInput("");
    setLoading(true);

    try {
      const response = await fetch("http://localhost:8000/api/chat/stream", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: question }),
      });

      if (!response.ok) {
        throw new Error("Failed to get response");
      }

      if (!response.body) {
        throw new Error("Streaming is not supported");
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder();

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;

        const chunk = decoder.decode(value, { stream: true });

        setMessages((prev) => {
          const updated = [...prev];
          const last = updated.length - 1;

          updated[last] = {
            ...updated[last],
            content: updated[last].content + chunk,
          };

          return updated;
        });
      }

      const remaining = decoder.decode();

      if (remaining) {
        setMessages((prev) => {
          const updated = [...prev];
          const last = updated.length - 1;

          updated[last] = {
            ...updated[last],
            content: updated[last].content + remaining,
          };

          return updated;
        });
      }
    } catch (error) {
      setMessages((prev) => {
        const updated = [...prev];
        const last = updated.length - 1;

        updated[last] = {
          ...updated[last],
          content: `Error: ${error.message}. Check that your backend is running.`,
        };

        return updated;
      });
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="chat">
      <header className="chat-header">
        <div className="logo">✦</div>
        <div>
          <h1>RAG Assistant</h1>
          <p>Retrieval-Augmented Generation</p>
        </div>
        <span className="status">● Ready</span>
      </header>

      <section className="messages">
        {messages.length === 0 && (
          <div className="welcome">
            <div className="welcome-icon">✦</div>
            <h2>Ask your knowledge anything.</h2>
            <p>Ask a question to start a conversation.</p>
          </div>
        )}

        {messages.map((message, index) => (
          <article
            className={`message ${message.role}`}
            key={index}
          >
            <span className="avatar">
              {message.role === "user" ? "You" : "AI"}
            </span>

            <div className="message-content">
              {message.content || (
                <span className="typing">Thinking...</span>
              )}
              {loading &&
                message.role === "assistant" &&
                index === messages.length - 1 && (
                  <span className="cursor">▍</span>
                )}
            </div>
          </article>
        ))}
      </section>

      <form className="composer" onSubmit={sendMessage}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask a question..."
          disabled={loading}
        />

        <button disabled={loading || !input.trim()}>
          {loading ? "..." : "↑"}
        </button>
      </form>

      <p className="disclaimer">
        AI-generated answers may contain mistakes.
      </p>
    </main>
  );
}