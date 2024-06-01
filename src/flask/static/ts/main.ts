document.getElementById('selectFolderButton')?.addEventListener('click', () => {
  selectFolder('inputFolder');
});

function selectFolder(inputId: string) {
  window.electron
    .selectFolder()
    .then((folderPath: string) => {
      const inputElement = document.getElementById(
        inputId,
      ) as HTMLInputElement | null;
      if (inputElement) {
        inputElement.value = folderPath;
      } else {
        console.error(`Element with id ${inputId} not found.`);
      }
    })
    .catch((err: Error) => {
      console.log(err);
    });
}
