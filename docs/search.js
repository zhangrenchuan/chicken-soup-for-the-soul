(() => {
  const input = document.querySelector('#find');
  if (!input) return;
  const grid = document.querySelector('#chapters');
  const results = document.querySelector('#results');
  const status = document.querySelector('#status');
  const rows = Array.from(results.children);
  const filter = () => {
    const words = input.value.trim().toLowerCase().split(/\s+/).filter(Boolean);
    grid.hidden = words.length > 0;
    results.hidden = words.length === 0;
    let count = 0;
    for (const row of rows) {
      const match = words.every(word => row.dataset.search.includes(word));
      row.hidden = !match;
      if (match) count++;
    }
    status.textContent = words.length ? (count ? '找到 ' + count + ' 篇笔记' : '没有找到相关笔记，试试其他关键词。') : '15 个章节 · 117 篇笔记';
  };
  input.addEventListener('input', filter);
  input.addEventListener('keydown', event => {
    if (event.key === 'Escape') {
      input.value = '';
      filter();
    }
  });
  filter();
})();
