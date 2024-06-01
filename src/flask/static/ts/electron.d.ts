interface Window {
    electron: {
      selectFolder: () => Promise<string>;
    };
  }