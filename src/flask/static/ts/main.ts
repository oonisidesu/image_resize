function selectFolder(inputId: string) {
  window.electron.selectFolder().then((folderPath: string) => {
    const inputElement = document.getElementById(inputId) as HTMLInputElement;
    if (inputElement) {
      inputElement.value = folderPath;
    } else {
      console.error(`Element with id ${inputId} not found.`);
    }
  }).catch((err: any) => {
    console.log(err);
  });
}