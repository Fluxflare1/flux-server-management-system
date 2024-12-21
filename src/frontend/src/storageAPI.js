const uploadFileToS3 = async (file, apiUrl) => {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(apiUrl, {
    method: "POST",
    body: formData,
  });

  return await response.json();
};

export default uploadFileToS3;
