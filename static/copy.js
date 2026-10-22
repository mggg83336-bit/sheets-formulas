// Adds a "Copy" button to every code block (formulas).
document.querySelectorAll("pre > code").forEach(function (code) {
  var b = document.createElement("button");
  b.className = "copy"; b.type = "button"; b.textContent = "Copy";
  b.addEventListener("click", function () {
    var t = code.innerText.trim();
    (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(
      function () { b.textContent = "Copied!"; setTimeout(function () { b.textContent = "Copy"; }, 1500); },
      function () { var r = document.createRange(); r.selectNodeContents(code); var s = getSelection(); s.removeAllRanges(); s.addRange(r); });
  });
  code.parentNode.appendChild(b);
});
