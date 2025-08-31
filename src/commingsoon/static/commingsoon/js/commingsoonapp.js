let days  = document.querySelector('.days')
let hours  = document.querySelector('.hours')
let minutes  = document.querySelector('.minutes')
let seconds  = document.querySelector('.seconds')

let targetDate = new Date("september 20 2025 00:00:00").getTime();

function timer() {
  let curentDate = new Date().getTime();
  let distance = targetDate - curentDate;

  let d = Math.floor(distance / 1000 / 60 / 60 / 24 );
  let h = Math.floor(distance / 1000 / 60 / 60 ) % 24 ;
  let m = Math.floor(distance / 1000 / 60  ) % 60;
  let s = Math.floor(distance / 1000  ) % 60;

  days.innerHTML = d;
  hours.innerHTML = h;
  minutes.innerHTML = m;
  seconds.innerHTML = s;
   if (distance < 0) {
      alert("time is over");
       
      days.innerHTML = "00";
      hours.innerHTML = "00";
      minutes.innerHTML = "00";
      seconds.innerHTML = "00";
    
   }
  
}
setInterval(timer , 1000);


