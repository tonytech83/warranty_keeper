// Client-side pagination for the supplier grid. The grid's column count is
// responsive (CSS `repeat(auto-fill, minmax(...))`, unknown until rendered),
// but we always want exactly 4 rows per page — so instead of a fixed
// server-side page size, all matching suppliers are rendered up front and
// this measures the actual rendered column count to slice them into pages.
(function () {
  var ROWS_PER_PAGE = 4;

  var list = document.getElementById("supplier-list");
  var pager = document.getElementById("supplier-pager");
  if (!list || !pager) return;

  var cards = Array.prototype.slice.call(list.children);
  if (!cards.length) return;

  var currentPage = 1;
  var resizeTimer = null;

  function getColumnCount() {
    var columns = getComputedStyle(list).gridTemplateColumns.split(" ").filter(Boolean);
    return Math.max(columns.length, 1);
  }

  function render() {
    var pageSize = getColumnCount() * ROWS_PER_PAGE;
    var totalPages = Math.max(Math.ceil(cards.length / pageSize), 1);
    if (currentPage > totalPages) currentPage = totalPages;

    var start = (currentPage - 1) * pageSize;
    var end = start + pageSize;
    cards.forEach(function (card, index) {
      card.hidden = index < start || index >= end;
    });

    renderPager(totalPages);
  }

  function renderPager(totalPages) {
    if (totalPages <= 1) {
      pager.hidden = true;
      pager.innerHTML = "";
      return;
    }
    pager.hidden = false;

    var html = "";
    html += pagerLink("‹ Prev", currentPage - 1, currentPage === 1, "pager-prev");
    for (var page = 1; page <= totalPages; page++) {
      if (page === currentPage) {
        html += '<span class="pager-link pager-current">' + page + "</span>";
      } else {
        html += pagerLink(String(page), page, false, "");
      }
    }
    html += pagerLink("Next ›", currentPage + 1, currentPage === totalPages, "pager-next");
    pager.innerHTML = html;

    pager.querySelectorAll("a[data-page]").forEach(function (link) {
      link.addEventListener("click", function (e) {
        e.preventDefault();
        currentPage = parseInt(link.dataset.page, 10);
        render();
        list.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    });
  }

  function pagerLink(label, page, disabled, extraClass) {
    var classes = "pager-link " + extraClass;
    if (disabled) {
      return '<span class="' + classes + ' pager-disabled">' + label + "</span>";
    }
    return '<a class="' + classes + '" href="#" data-page="' + page + '">' + label + "</a>";
  }

  window.addEventListener("resize", function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(render, 200);
  });

  render();
})();
