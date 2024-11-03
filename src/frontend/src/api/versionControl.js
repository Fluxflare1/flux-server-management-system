// src/frontend/src/api/versionControl.js
import axiosInstance from "./axiosInstance";

export const cloneRepository = (repoUrl) => axiosInstance.post("/git/clone/", { repo_url: repoUrl });
