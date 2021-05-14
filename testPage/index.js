let users;
let timer = 15;

let timerInterval;

const firstTableData = document.getElementById('first_table_data');
const timerNode = document.getElementById('timer');
const updateTimerButton = document.getElementById('button-addon2');

const loadData = async () => {
  const res = await fetch('https://jsonplaceholder.typicode.com/users');
  const data = await res.json();
  users = data;
};

const startTimer = () => {
  timer = 15;
  timerInterval = setInterval(() => {
    timerNode.innerHTML = timer + ' seconds';

    if (timer === 0) {
      clearInterval(timerInterval);
      setTimeout(() => alert('ты победил'), 100);
    } else {
      timer--;
    }
  }, 1000);
};

window.addEventListener('load', async () => {
  await loadData();

  if (!!users) {
    firstTableData.innerHTML = users[0].phone;
  }

  startTimer();

  updateTimerButton.addEventListener('click', () => {
    clearInterval(timerInterval);
    startTimer();
  });
});
