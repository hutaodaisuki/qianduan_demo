const form = document.getElementById('commentForm');
const nameInput = document.getElementById('name');
const emailInput = document.getElementById('email');
const contentInput = document.getElementById('content');
const successMsg = document.getElementById('successMsg');
const commentsContainer = document.getElementById('commentsContainer');

const nameGroup = document.getElementById('nameGroup');
const emailGroup = document.getElementById('emailGroup');
const contentGroup = document.getElementById('contentGroup');
const nameError = document.getElementById('nameError');
const emailError = document.getElementById('emailError');
const contentError = document.getElementById('contentError');

function showError(group, errorElement, message) {
  group.classList.add('error');
  errorElement.textContent = message;
}

function hideError(group) {
  group.classList.remove('error');
}

function validateEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function validateForm() {
  let isValid = true;

  if (!nameInput.value.trim()) {
    showError(nameGroup, nameError, '姓名不能为空');
    isValid = false;
  } else {
    hideError(nameGroup);
  }

  if (!emailInput.value.trim() || !validateEmail(emailInput.value)) {
    showError(emailGroup, emailError, '请输入有效的邮箱地址');
    isValid = false;
  } else {
    hideError(emailGroup);
  }

  if (!contentInput.value.trim() || contentInput.value.length < 5) {
    showError(contentGroup, contentError, '留言内容长度不少于5个字');
    isValid = false;
  } else {
    hideError(contentGroup);
  }

  return isValid;
}

function clearForm() {
  nameInput.value = '';
  emailInput.value = '';
  contentInput.value = '';
  hideError(nameGroup);
  hideError(emailGroup);
  hideError(contentGroup);
}

function saveComment(comment) {
  const comments = JSON.parse(localStorage.getItem('comments') || '[]');
  comments.unshift(comment);
  localStorage.setItem('comments', JSON.stringify(comments));
}

function loadComments() {
  const comments = JSON.parse(localStorage.getItem('comments') || '[]');
  if (comments.length === 0) {
    commentsContainer.innerHTML = '<div class="empty-state">暂无留言，快来发表第一条留言吧！</div>';
    return;
  }

  let html = '';
  comments.forEach(comment => {
    html += `
      <div class="comment-item">
        <div class="comment-header">
          <div>
            <span class="comment-author">👤 ${comment.name}</span>
            <span class="comment-email">${comment.email}</span>
          </div>
          <span class="comment-date">📅 ${comment.date}</span>
        </div>
        <div class="comment-content">${comment.content}</div>
      </div>
    `;
  });
  commentsContainer.innerHTML = html;
}

function showSuccessMessage() {
  successMsg.classList.add('show');
  setTimeout(() => {
    successMsg.classList.remove('show');
  }, 3000);
}

form.addEventListener('submit', function(e) {
  e.preventDefault();

  if (!validateForm()) {
    return;
  }

  const comment = {
    name: nameInput.value.trim(),
    email: emailInput.value.trim(),
    content: contentInput.value.trim(),
    date: new Date().toLocaleString('zh-CN')
  };

  saveComment(comment);
  clearForm();
  showSuccessMessage();
  loadComments();
});

document.addEventListener('DOMContentLoaded', loadComments);