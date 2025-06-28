import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import api from "../api";
import PublicLink from "../components/PublicLink";

function PublicLinks() {
  const { username } = useParams();
  const [links, setLinks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    api
      .get(`/links/public/${username}/`)
      .then((res) => {
        setLinks(res.data);
        setLoading(false);
      })
      .catch(() => {
        setError("Failed to load public links.");
        setLoading(false);
      });
  }, [username]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>{error}</p>;
  if (links.length === 0) return <p>No public links found for {username}</p>;

  return (
    <div className="container">
      <h2>{username}'s Public Links</h2>
      <div className="link-list">
        {links.map((link) => (
          <PublicLink link={link} key={link.id} />
        ))}
      </div>
    </div>
  );
}

export default PublicLinks;
