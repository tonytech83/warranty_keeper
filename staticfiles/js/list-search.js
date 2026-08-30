// Debounced auto-submit for a list page's search box (warranties, suppliers).
// Filtering/sorting happens server-side (see the view's get_queryset), so
// typing re-submits the surrounding GET form after a short pause instead of
// filtering rows already on the page — this keeps search correct across
// paginated results instead of only the currently loaded page.
(function () {
  var input = document.querySelector(".search-input");
  if (!input) return;

  var form = input.closest("form");
  if (!form) return;

  var DEBOUNCE_MS = 400;
  var timer = null;

  input.addEventListener("input", function () {
    clearTimeout(timer);
    timer = setTimeout(function () {
      if (form.requestSubmit) {
        form.requestSubmit();
      } else {
        form.submit();
      }
    }, DEBOUNCE_MS);
  });

  // Restore focus/cursor after the page reloads from a search submission.
  if (input.value) {
    input.focus();
    var end = input.value.length;
    input.setSelectionRange(end, end);
  }
})();
