import { useState, useEffect } from "react";
import api from "../api";
import Link from "../components/Link";
import "../styles/Home.css";

function Home() {
  const [links, setLinks] = useState([]);
  const [url, setUrl] = useState("");
  const [platform, setPlatform] = useState("");

  useEffect(() => {
    getLinks();
  }, []);

  const getLinks = () => {
    api
      .get("/links/list/")
      .then((res) => res.data)
      .then((data) => {
        setLinks(data);
      })
      .catch((err) => alert(err));
  };

  const deleteLink = (id) => {
    api
      .delete(`/links/delete/${id}/`)
      .then((res) => {
        if (res.status === 204) alert("Link was deleted.");
        else alert("Failed to delete link.");
        getLinks();
      })
      .catch((error) => alert(error));
  };

  const createLink = (e) => {
    e.preventDefault();
    api
      .post("/links/add/", { url, platform })
      .then((res) => {
        if (res.status === 201) {
          alert("Link was saved.");
          setUrl("");
          setPlatform("");
        } else {
          alert("Failed to save link.");
        }
        getLinks();
      })
      .catch((error) => alert(error));
  };

  return (
    <div className="container">
      <div className="top-bar">
        <a href="/logout/" className="logout-button">Logout</a>
      </div>

      <div className="qr-button-wrapper">
        <button className="qr-button">MyQRCode</button>
      </div>

      <div>
        <h2>Links</h2>
        <div className="link-list">
          {links.map((link) => (
            <Link link={link} onDelete={deleteLink} key={link.id} />
          ))}
        </div>
      </div>

      <h2>Add a link</h2>
      <form onSubmit={createLink}>
        <label htmlFor="platform">Platform:</label>
        <input
          type="text"
          id="platform"
          name="platform"
          required
          onChange={(e) => setPlatform(e.target.value)}
          value={platform}
        />
        <label htmlFor="url">URL:</label>
        <input
          type="url"
          id="url"
          name="url"
          required
          onChange={(e) => setUrl(e.target.value)}
          value={url}
        />
        <input type="submit" value="submit" />
      </form>
    </div>
  );
}

export default Home;
