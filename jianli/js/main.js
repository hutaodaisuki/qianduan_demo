/**
 * 个人简历 · WebGIS 方向 — 交互脚本
 */

(function () {
  'use strict';

  // ===== 1. 技能标签：添加等级说明 =====
  const levelMap = {
    'level-advanced': { label: '精通', color: '#0d47a1' },
    'level-intermediate': { label: '掌握', color: '#1557b0' },
    'level-familiar': { label: '熟悉', color: '#5a6674' }
  };

  function initSkillTags() {
    const tags = document.querySelectorAll('.skill-tag');
    tags.forEach(tag => {
      // 为有 level 类别的标签添加 data-tip，鼠标悬停时显示等级
      for (const [cls, info] of Object.entries(levelMap)) {
        if (tag.classList.contains(cls)) {
          tag.setAttribute('data-tip', info.label);
          tag.title = info.label;
          break;
        }
      }
    });
  }

  // ===== 2. 项目卡片：滚动进入视口时淡入动画 =====
  function initProjectAnimations() {
    const projects = document.querySelectorAll('.project');
    if (!('IntersectionObserver' in window)) {
      // 不支持时直接显示
      projects.forEach(p => p.style.opacity = '1');
      return;
    }

    projects.forEach(p => {
      p.style.opacity = '0';
      p.style.transform = 'translateY(20px)';
      p.style.transition = 'opacity 0.6s ease, transform 0.6s ease, border-color 0.25s, box-shadow 0.25s';
    });

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    projects.forEach(p => observer.observe(p));
  }

  // ===== 3. 打印快捷按钮（双击页脚触发） =====
  function initPrintShortcut() {
    const footer = document.querySelector('.footer');
    if (footer) {
      footer.style.cursor = 'pointer';
      footer.title = '双击此处打印简历';
      footer.addEventListener('dblclick', () => {
        window.print();
      });
    }
  }

  // ===== 4. 平滑锚点滚动（如果将来加导航） =====
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function (e) {
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }

  // ===== 初始化 =====
  function init() {
    initSkillTags();
    initProjectAnimations();
    initPrintShortcut();
    initSmoothScroll();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
