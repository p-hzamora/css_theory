Math
const $indicator = document.querySelector(".indicator")
const r = 15;
const R = 35;
const increments = calc_circles(r,R)
console.log(increments)
$indicator.style.setProperty('--r',r+"px");
$indicator.style.setProperty('--R',R+"px");
$indicator.style.setProperty("--x",increments.x+"px");
$indicator.style.setProperty("--y",increments.y+"px");


function calc_circles(r=15,R=35){
    const degree= Math.asin(r/(r+R));
    const increment = R * (1-Math.cos(degree));
    const x = 2*r - increment;
    
    const y = 2*r-(R * Math.sin(degree));
    return {x, y}
}