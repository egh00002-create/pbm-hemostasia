import { useEffect } from 'react';
import { useLocalStorage } from './useLocalStorage';

export type ThemePref = 'light' | 'dark' | 'auto';

/** Preferencia de tema (claro por defecto), persistida y aplicada al <html>. */
export function useTheme() {
  const [pref, setPref] = useLocalStorage<ThemePref>('pbm_theme', 'light');

  useEffect(() => {
    const root = document.documentElement;
    const apply = () => {
      let effective: 'light' | 'dark' = 'light';
      if (pref === 'auto') {
        effective = window.matchMedia('(prefers-color-scheme: dark)').matches
          ? 'dark'
          : 'light';
      } else {
        effective = pref;
      }
      root.setAttribute('data-theme', effective);
      const meta = document.querySelector('meta[name="theme-color"]');
      if (meta) meta.setAttribute('content', effective === 'dark' ? '#181113' : '#8E2433');
    };
    apply();
    if (pref === 'auto') {
      const mq = window.matchMedia('(prefers-color-scheme: dark)');
      mq.addEventListener('change', apply);
      return () => mq.removeEventListener('change', apply);
    }
  }, [pref]);

  const cycle = () => setPref(pref === 'light' ? 'dark' : pref === 'dark' ? 'auto' : 'light');

  return { pref, setPref, cycle };
}
