const accountToggle = document.querySelector('.account-toggle');
const accountPanel = document.querySelector('.account-panel');
const accountOverlay = document.querySelector('.account-overlay');
const accountClose = document.querySelector('.account-close');

if (accountToggle && accountPanel && accountOverlay && accountClose) {

    function openAccountPanel() {
        accountPanel.classList.add('open');
        accountOverlay.classList.add('open');

        accountToggle.setAttribute('aria-expanded', 'true');
        accountPanel.setAttribute('aria-hidden', 'false');
    }

    function closeAccountPanel() {
        accountPanel.classList.remove('open');
        accountOverlay.classList.remove('open');

        accountToggle.setAttribute('aria-expanded', 'false');
        accountPanel.setAttribute('aria-hidden', 'true');
    }

    accountToggle.addEventListener('click', function () {
        if (accountPanel.classList.contains('open')) {
            closeAccountPanel();
        } else {
            openAccountPanel();
        }
    });

    accountClose.addEventListener('click', closeAccountPanel);
    accountOverlay.addEventListener('click', closeAccountPanel);

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape') {
            closeAccountPanel();
        }
    });
}