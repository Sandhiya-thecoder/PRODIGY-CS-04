const logArea = document.getElementById("logArea");

document.addEventListener("keydown", (event) => {
  let key = event.key;

  // Format special keys
  if (key === " ") key = "[SPACE]";
  else if (key === "Enter") key = "[ENTER]";
  else if (key === "Backspace") key = "[BACKSPACE]";
  else if (key.length > 1) key = `[${key.toUpperCase()}]`;

  logArea.value += key;
});
