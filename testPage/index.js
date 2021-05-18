let users;
let timer = 15;

let timerInterval;

const firstTableData = document.getElementById('first_table_data');
const timerNode = document.getElementById('timer');
const updateTimerButton = document.getElementById('button-addon2');



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

const tbody = document.getElementById('tbody');
for ( i = 1; i < 12; i++) {
  
  let index = i
  let sum = []
  console.log(sum)
  let username = ["dima","nikita","stas","gena","ira","nikolay","petr","ivan","akakiy","evgeniy","kolya","max"]
  tbody.innerHTML += `
<tr>
                <th scope="row">${index}</th>
                <td>${username[i]}</td>
                <td>${sum.sort((a,b)=> b-a)}</td>
              </tr>

              `




}

