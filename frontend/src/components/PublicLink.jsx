import React from "react";
import "../styles/Link.css";

function PublicLink({ link }) {
  const formattedDate = new Date(link.created_at).toLocaleDateString("en-US");

  return (
    <div className="link-container">
      <p className="link-title">{link.platform}</p>
      <p className="link-content">
        <a href={link.url} target="_blank" rel="noopener noreferrer">
          {link.url}
        </a>
      </p>
      <p className="link-date">{formattedDate}</p>
    </div>
  );
}

export default PublicLink;
