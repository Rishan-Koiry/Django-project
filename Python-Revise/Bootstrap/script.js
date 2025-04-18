let disabled = false;
const button = document.getElementById("button");
const canvas = document.getElementById("canvas");
const ctx = canvas.getContext("2d");
let confetti = [];
let sequins = [];

// Set up canvas
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
let cx = ctx.canvas.width / 2;
let cy = ctx.canvas.height / 2;

// Animation constants
const confettiCount = 150; // Increased for more density
const sequinCount = 80;
const gravityConfetti = 0.25;
const gravitySequins = 0.45;
const dragConfetti = 0.05;
const dragSequins = 0.02;
const terminalVelocity = 3;

// Flag to track first visit
let firstVisit = true;

// Check for previous visits using localStorage
if (localStorage.getItem("hasVisited")) {
  // firstVisit = false;
} else {
  // Set the flag to indicate this is not the first visit anymore
  localStorage.setItem("hasVisited", "true");
}

// Holi colors - vibrant gulal powder colors
const colors = [
  { front: "#FF1744", back: "#D50000" }, // Red
  { front: "#FFEA00", back: "#FFD600" }, // Yellow
  { front: "#00E676", back: "#00C853" }, // Green
  { front: "#2979FF", back: "#2962FF" }, // Blue
  { front: "#D500F9", back: "#AA00FF" }, // Purple
  { front: "#FF9100", back: "#FF6D00" }, // Orange
  { front: "#F06292", back: "#EC407A" }, // Pink (gulabi)
  { front: "#18FFFF", back: "#00E5FF" }, // Cyan
];

// Helper function for random numbers
function randomRange(min, max) {
  return Math.random() * (max - min) + min;
}

// Initial velocity for powder particles
function initConfettoVelocity(xRange, yRange) {
  const x = randomRange(xRange[0], xRange[1]);
  const range = yRange[1] - yRange[0] + 1;
  let y =
    yRange[1] - Math.abs(randomRange(0, range) + randomRange(0, range) - range);
  if (y >= yRange[1] - 1) {
    y += Math.random() < 0.25 ? randomRange(1, 3) : 0;
  }
  return { x: x, y: -y };
}

// Helper to convert hex to rgb
function hexToRgb(hex) {
  hex = hex.replace("#", "");
  const r = parseInt(hex.substring(0, 2), 16);
  const g = parseInt(hex.substring(2, 4), 16);
  const b = parseInt(hex.substring(4, 6), 16);
  return `${r}, ${g}, ${b}`;
}

// Confetto constructor - represents larger powder particles
function Confetto() {
  this.randomModifier = randomRange(0, 99);
  this.color = colors[Math.floor(randomRange(0, colors.length))];

  // More varied shapes for powder look
  this.isCircular = Math.random() < 0.7;

  if (this.isCircular) {
    this.dimensions = {
      x: randomRange(5, 9),
      y: randomRange(5, 9),
    };
  } else {
    this.dimensions = {
      x: randomRange(4, 10),
      y: randomRange(3, 8),
    };
  }

  // Enhanced texture properties
  this.noiseLevel = randomRange(0.2, 0.9);
  this.initialOpacity = randomRange(0.7, 1.0);
  this.opacity = this.initialOpacity;
  this.matteFactor = randomRange(0.5, 0.9);

  // Position and movement
  this.position = {
    x: randomRange(
      canvas.width / 2 - button.offsetWidth / 3,
      canvas.width / 2 + button.offsetWidth / 3
    ),
    y: randomRange(
      canvas.height / 2 + button.offsetHeight / 2,
      canvas.height / 2 + 1.5 * button.offsetHeight
    ),
  };
  this.rotation = randomRange(0, 2 * Math.PI);
  this.scale = { x: 1, y: 1 };
  this.velocity = initConfettoVelocity([-12, 12], [10, 16]); // Enhanced velocity
}

// Update confetto physics
Confetto.prototype.update = function () {
  // Apply forces with randomness for natural dispersion
  this.velocity.x -= this.velocity.x * dragConfetti;
  this.velocity.y = Math.min(
    this.velocity.y + gravityConfetti,
    terminalVelocity
  );

  // Add unpredictable movement
  if (Math.random() > 0.9) {
    this.velocity.x +=
      (Math.random() > 0.5 ? 0.3 : -0.3) * randomRange(0.5, 1.5);
  }

  // Update position
  this.position.x += this.velocity.x;
  this.position.y += this.velocity.y;

  // Adjust scale for 3D effect
  this.scale.y = Math.max(
    0.1,
    Math.cos((this.position.y + this.randomModifier) * 0.09) * this.matteFactor
  );

  // Decrease opacity for fade effect
  this.opacity = Math.max(0, this.opacity - 0.006 * randomRange(0.95, 1.05));

  // Air resistance
  if (Math.abs(this.velocity.x) > 0.1) {
    this.velocity.x *= 0.99;
  }
};

// Sequin constructor - represents tiny powder particles
function Sequin() {
  this.color = colors[Math.floor(randomRange(0, colors.length))].front;
  this.radius = randomRange(1, 3);
  this.position = {
    x: randomRange(
      canvas.width / 2 - button.offsetWidth / 3,
      canvas.width / 2 + button.offsetWidth / 3
    ),
    y: randomRange(
      canvas.height / 2 + button.offsetHeight / 2,
      canvas.height / 2 + 1.5 * button.offsetHeight
    ),
  };
  this.velocity = {
    x: randomRange(-8, 8),
    y: randomRange(-10, -14),
  };
  this.opacity = randomRange(0.8, 1.0);
  this.grainFactor = randomRange(0.85, 0.95);
}

// Update sequin physics
Sequin.prototype.update = function () {
  // Apply forces with randomness
  this.velocity.x -= this.velocity.x * dragSequins;
  this.velocity.y = this.velocity.y + gravitySequins;

  // Random movement
  if (Math.random() > 0.9) {
    this.velocity.x += Math.random() > 0.5 ? 0.2 : -0.2;
  }

  // Update position
  this.position.x += this.velocity.x;
  this.position.y += this.velocity.y;

  // Fade effect
  this.opacity = Math.max(0, this.opacity - 0.01 * this.grainFactor);
};

// Initialize particles
function initBurst() {
  for (let i = 0; i < confettiCount; i++) {
    confetti.push(new Confetto());
  }
  for (let i = 0; i < sequinCount; i++) {
    sequins.push(new Sequin());
  }
}

function render() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Draw confetti (larger particles)
  confetti.forEach((confetto) => {
    let width = confetto.dimensions.x * confetto.scale.x;
    let height = confetto.dimensions.y * confetto.scale.y;

    // Position and rotate
    ctx.save();
    ctx.translate(confetto.position.x, confetto.position.y);
    ctx.rotate(confetto.rotation);

    // Update physics
    confetto.update();

    // Set fill color with opacity
    const colorRgb = hexToRgb(
      confetto.scale.y > 0 ? confetto.color.front : confetto.color.back
    );
    ctx.fillStyle = `rgba(${colorRgb}, ${confetto.opacity})`;

    // Draw appropriate shape
    if (confetto.isCircular) {
      // Circular particle
      ctx.beginPath();
      ctx.arc(0, 0, width / 2, 0, 2 * Math.PI);
      ctx.fill();

      // Add texture with dots
      if (confetto.noiseLevel > 0.5) {
        const dotCount = Math.floor(randomRange(3, 7));
        for (let i = 0; i < dotCount; i++) {
          const dotX = randomRange(-width / 3, width / 3);
          const dotY = randomRange(-height / 3, height / 3);
          const dotSize = randomRange(0.5, 1.5);

          ctx.fillStyle = `rgba(${colorRgb}, ${confetto.opacity * 0.7})`;
          ctx.beginPath();
          ctx.arc(dotX, dotY, dotSize, 0, 2 * Math.PI);
          ctx.fill();
        }
      }
    } else {
      // Irregular shape
      ctx.beginPath();
      const sides = Math.floor(randomRange(5, 8));
      const startAngle = Math.random() * Math.PI * 2;

      for (let i = 0; i < sides; i++) {
        const angle = startAngle + (i * 2 * Math.PI) / sides;
        const radius = (width / 2) * (0.8 + Math.random() * 0.4);

        const x = Math.cos(angle) * radius;
        const y = Math.sin(angle) * radius;

        if (i === 0) {
          ctx.moveTo(x, y);
        } else {
          ctx.lineTo(x, y);
        }
      }

      ctx.closePath();
      ctx.fill();
    }

    ctx.restore();
  });

  sequins.forEach((sequin) => {
    ctx.save();
    ctx.translate(sequin.position.x, sequin.position.y);

    // Update physics
    sequin.update();

    // Set color with opacity
    ctx.fillStyle = `rgba(${hexToRgb(sequin.color)}, ${sequin.opacity})`;

    // Draw tiny particle
    ctx.beginPath();
    ctx.arc(0, 0, sequin.radius, 0, 2 * Math.PI);
    ctx.fill();

    // Add texture
    if (Math.random() > 0.7) {
      ctx.fillStyle = `rgba(${hexToRgb(sequin.color)}, ${
        sequin.opacity * 0.6
      })`;
      ctx.beginPath();
      ctx.arc(
        randomRange(-0.5, 0.5),
        randomRange(-0.5, 0.5),
        sequin.radius * 0.5,
        0,
        2 * Math.PI
      );
      ctx.fill();
    }

    ctx.restore();
  });

  confetti = confetti.filter(
    (c) => c.position.y < canvas.height && c.opacity > 0.1
  );
  sequins = sequins.filter(
    (s) => s.position.y < canvas.height && s.opacity > 0.1
  );
  requestAnimationFrame(render);
}

function clickButton() {
  if (!disabled) {
    disabled = true;
    // Loading stage
    button.classList.add("loading");
    button.classList.remove("ready");
    setTimeout(() => {
      // Completed stage
      button.classList.add("complete");
      button.classList.remove("loading");
      setTimeout(() => {
        // Create the burst
        initBurst();
        setTimeout(() => {
          // Reset button
          disabled = false;
          button.classList.add("ready");
          button.classList.remove("complete");
        }, 4000);
      }, 320);
    }, 1800);
  }
}

// Event listener for manual button click
button.addEventListener("click", clickButton);

// Auto-click function that triggers on first load
function autoClickOnFirstLoad() {
  // Use a short delay to ensure everything is loaded properly
  setTimeout(() => {
    // Check if this is the first visit
    if (firstVisit) {
      clickButton();
    }
  }, 1000); // Delay of 1 second before auto-clicking
}

// Call the function when the page loads
window.addEventListener("load", autoClickOnFirstLoad);

function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  cx = ctx.canvas.width / 2;
  cy = ctx.canvas.height / 2;
}

window.addEventListener("resize", resizeCanvas);

document.body.onkeyup = (e) => {
  if (e.keyCode == 13 || e.keyCode == 32) {
    clickButton();
  }
};

const textElements = button.querySelectorAll(".button-text");
textElements.forEach((element) => {
  const characters = element.innerText.split("");
  let characterHTML = "";
  characters.forEach((letter, index) => {
    characterHTML += `<span class="char${index}" style="--d:${
      index * 30
    }ms; --dr:${(characters.length - index - 1) * 30}ms;">${letter}</span>`;
  });
  element.innerHTML = characterHTML;
});

requestAnimationFrame(render);

(function () {
  // Create the HTML for social links
  const socialLinksHTML = `
    <div class="social-links-custom">
        <a href="https://x.com/stejas809" target="_blank" title="Twitter/X">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4l11.733 16h4.267l-11.733 -16z"/><path d="M4 20l6.768 -6.768m2.46 -2.46l6.772 -6.772"/></svg>
        </a>
        <a href="https://www.linkedin.com/in/tejas-shah-b22490156/" target="_blank" title="LinkedIn">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
        </a>
        <a href="https://imaginea.store" target="_blank" title="Imaginea Store">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>
        </a>
        <a href="https://www.reddit.com/user/Business-Study9412/" target="_blank" title="Reddit">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><path d="M16.5,7.5 C16.5,6.7 15.8,6 15,6 C14.2,6 13.5,6.7 13.5,7.5 C13.5,8.3 14.2,9 15,9 C15.8,9 16.5,8.3 16.5,7.5 Z"></path><path d="M8.5,9 C9.3,9 10,8.3 10,7.5 C10,6.7 9.3,6 8.5,6 C7.7,6 7,6.7 7,7.5 C7,8.3 7.7,9 8.5,9 Z"></path><path d="M15,9 C15,12 12.5,14 10,14 C7.5,14 5,12 5,9"></path></svg>
        </a>
        <a href="mailto:ceo@imaginea.store" title="Email">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>
        </a>
    </div>
  `;

  // Create the CSS for social links
  const socialLinksCSS = `
    .social-links-custom {
      position: fixed;
      top: 20px;
      right: 20px;
      display: flex;
      gap: 15px;
      z-index: 10;
    }

    .social-links-custom a {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.8);
      color: #333;
      transition: all 0.3s ease;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    }

    .social-links-custom a:hover {
      transform: translateY(-3px);
      background: white;
      box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
    }

    @media (max-width: 768px) {
      .social-links-custom {
        top: 10px;
        right: 10px;
        gap: 10px;
      }
      
      .social-links-custom a {
        width: 35px;
        height: 35px;
      }
      
      .social-links-custom svg {
        width: 20px;
        height: 20px;
      }
    }
  `;

  // Function to create and inject the stylesheet
  function injectCSS(css) {
    const style = document.createElement("style");
    style.textContent = css;
    document.head.appendChild(style);
  }

  // Function to create and inject the HTML
  function injectHTML(html) {
    const div = document.createElement("div");
    div.innerHTML = html;
    document.body.appendChild(div.firstElementChild);
  }

  // Check if document is loaded, then inject
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      injectCSS(socialLinksCSS);
      injectHTML(socialLinksHTML);
    });
  } else {
    injectCSS(socialLinksCSS);
    injectHTML(socialLinksHTML);
  }
})();
