// Dark mode toggle
document.getElementById('darkModeToggle').addEventListener('click', () => {
  document.body.classList.toggle('dark');
});

// Search filter
document.getElementById('search').addEventListener('input', function () {
  const searchText = this.value.toLowerCase();
  const cards = document.querySelectorAll('.card');

  cards.forEach(card => {
    const content = card.innerText.toLowerCase();
    if (content.includes(searchText)) {
      card.style.display = 'block';
    } else {
      card.style.display = 'none';
    }
  });
});