// Declare variables to store custom counts
let customWordCount;
let customSentenceCount;

// Get the select element
const summaryLengthSelect = document.getElementById('summary-length');

// Get the element to display the custom counts
const customCountDisplay = document.getElementById('custom-count-display');

// Add event listener for change event
summaryLengthSelect.addEventListener('change', function() {
  const selectedValue = summaryLengthSelect.value;

  // Check if the custom word count option is selected
  if (selectedValue === 'custom-word') {
    customWordCount = prompt('Enter the custom word count:');
    customCountDisplay.textContent = 'Custom word count: ' + customWordCount;
  }

  // Check if the custom sentence count option is selected
  if (selectedValue === 'custom-sentence') {
    customSentenceCount = prompt('Enter the custom sentence count:');
    customCountDisplay.textContent = 'Custom sentence count: ' + customSentenceCount;
  }
});

// Example usage outside of the event listener
function summarizeText() {
  // Use the custom word count or custom sentence count values as needed
  console.log('Custom word count:', customWordCount);
  console.log('Custom sentence count:', customSentenceCount);

  // Replace the following line with the code to generate the summary
  const generatedSummary = ""; // Provide the generated summary here
  updateSummary(generatedSummary);
}

// Get the input elements
document.addEventListener('DOMContentLoaded', function() {
  // Get the necessary elements
  const textInput = document.getElementById('text-input');
  const wordCount = document.getElementById('word-count');
  const warningMessage = document.getElementById('warning-message');
  const summarizeButton = document.getElementById('summarize-button');

  // Function to update the word count
  function updateWordCount() {
    const textValue = textInput.value.trim();
    const words = textValue.trim().split(/\s+/);
    const wordCountValue = words.length;
    console.log(wordCountValue);
    wordCount.textContent = `Words entered: ${wordCountValue}`;

    if (wordCountValue > 1000) {
      warningMessage.style.display = 'block';
    } else {
      warningMessage.style.display = 'none';
    }
  }
  
  // Add event listener to the input element
  textInput.addEventListener('input', updateWordCount);

  // Add event listener to the summarize button
  summarizeButton.addEventListener('click', function(event) {
    event.preventDefault(); // Prevent form submission
    summarizeText(); // Call the summarizeText function
  });
});

function updateSummary(summary) {
  const summaryElement = document.getElementById('summary-text');
  console.log(summary); // Log the summary value
  summaryElement.textContent = summary;
}

// Call the updateSummary function with the generated summary
const generatedSummary = ""; // Replace with the generated summary data
updateSummary(generatedSummary);
