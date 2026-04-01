// static/script.js
document.addEventListener('DOMContentLoaded', () => {
    const translateBtn = document.getElementById('translate-btn');
    const textInput = document.getElementById('text-input');
    const sourceLang = document.getElementById('source-lang');
    const targetLang = document.getElementById('target-lang');
    
    const resultSection = document.getElementById('result-section');
    const outputTranslation = document.getElementById('output-translation');
    const outputPronunciation = document.getElementById('output-pronunciation');
    const audioContainer = document.getElementById('audio-container');
    const audioPlayer = document.getElementById('audio-player');
    
    const errorBanner = document.getElementById('error-banner');
    const btnText = document.querySelector('.btn-text');
    const loader = document.querySelector('.loader');

    translateBtn.addEventListener('click', async () => {
        const textToTranslate = textInput.value.trim();
        
        if (!textToTranslate) {
            showError("Please enter some text to translate.");
            return;
        }

        // UI Loading State
        setLoadingState(true);

        try {
            const response = await fetch('/api/translate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    text: textToTranslate,
                    source_language: sourceLang.value,
                    target_language: targetLang.value
                })
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || "Failed to translate");
            }

            // Success Updates
            outputTranslation.textContent = data.translation;
            outputPronunciation.textContent = data.pronunciation || "N/A";
            
            if (data.audio_url) {
                audioPlayer.src = data.audio_url;
                audioContainer.classList.remove('hidden');
                audioPlayer.load();
            } else {
                audioContainer.classList.add('hidden');
            }

            resultSection.classList.remove('hidden');

        } catch (error) {
            showError(`Error during translation: ${error.message}`);
        } finally {
            // Revert state
            setLoadingState(false);
        }
    });

    function setLoadingState(isLoading) {
        if (isLoading) {
            btnText.textContent = "Translating...";
            loader.classList.remove('hidden');
            translateBtn.disabled = true;
            errorBanner.classList.add('hidden');
            resultSection.classList.add('hidden');
        } else {
            btnText.textContent = "🚀 Translate Now";
            loader.classList.add('hidden');
            translateBtn.disabled = false;
        }
    }

    function showError(msg) {
        errorBanner.textContent = msg;
        errorBanner.classList.remove('hidden');
        resultSection.classList.add('hidden');
    }
});
