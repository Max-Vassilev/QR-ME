import React from "react";
import "../styles/Link.css";

function Link({ link, onDelete }) {
  const formattedDate = new Date(link.created_at).toLocaleDateString("en-US");

  return (
    <div className="link-container">
      <p className="link-title">{link.platform}</p>
      <p className="link-content">{link.url}</p>
      <p className="link-date">{formattedDate}</p>
      <button className="delete-button" onClick={() => onDelete(link.id)}>
        Delete
      </button>
    </div>
  );
}

export default Link;