import { describe, it, expect } from 'vitest';
import { render, screen, fireEvent } from '@testing-library/react';
import { AnemiaDxCalc } from './AnemiaDxCalc';
import { FeEpoElectivaCalc } from './FeEpoElectivaCalc';
import { FeEpoUrgenteCalc } from './FeEpoUrgenteCalc';

const set = (label: RegExp, value: string) => fireEvent.change(screen.getByLabelText(label), { target: { value } });

describe('Pantallas de ferropenia — regresión Fase 2a', () => {
  it('AnemiaDx: IST no numérica bloquea el resultado (no "normal")', () => {
    render(<AnemiaDxCalc />);
    set(/IST/, 'abc');
    expect(screen.getByRole('alert')).toHaveTextContent('Valor no válido en: IST');
    expect(screen.queryByText(/Diagnóstico férrico/)).toBeNull();
  });

  it('AnemiaDx: ferritina negativa bloquea el resultado', () => {
    render(<AnemiaDxCalc />);
    set(/Ferritina/, '-5');
    expect(screen.getByRole('alert')).toHaveTextContent('Ferritina');
    expect(screen.queryByText(/Diagnóstico férrico/)).toBeNull();
  });

  it('AnemiaDx: caso 70 / IST 24 → "inflamación no evaluada" + DERIVAR', () => {
    render(<AnemiaDxCalc />);
    set(/Ferritina/, '70');
    set(/IST/, '24');
    expect(screen.getByText(/inflamación no evaluada \(PCR no aportada\)/)).toBeInTheDocument();
    expect(screen.getByText(/DERIVAR/)).toBeInTheDocument();
  });

  it('Electiva: caso 70 / IST 24 → DERIVAR, sin pauta', () => {
    render(<FeEpoElectivaCalc />);
    set(/Hemoglobina/, '10.5');
    set(/Ferritina/, '70');
    set(/IST/, '24');
    expect(screen.getByText(/DERIVAR a M. Interna/)).toBeInTheDocument();
    expect(screen.queryByText(/Hierro IV:/)).toBeNull();
  });

  it('Electiva: IST inválida bloquea (antes se saltaba la derivación y se pautaba)', () => {
    render(<FeEpoElectivaCalc />);
    set(/IST/, '24%');
    expect(screen.getByRole('alert')).toHaveTextContent('IST');
    expect(screen.queryByText(/Hierro IV:/)).toBeNull();
  });

  it('Electiva: IST vacía → sin pauta (antes pautaba la matriz)', () => {
    render(<FeEpoElectivaCalc />);
    set(/IST/, '');
    expect(screen.getByText(/IST necesaria para aplicar la matriz de tratamiento o descartar derivación/)).toBeInTheDocument();
    expect(screen.queryByText(/Hierro IV:/)).toBeNull();
  });

  it('Urgente: caso 70 / IST 24 → fuera de la Figura 13, sin hierro ni EPO', () => {
    render(<FeEpoUrgenteCalc />);
    set(/Hemoglobina/, '10.5');
    set(/Ferritina/, '70');
    set(/IST/, '24');
    expect(screen.getByText(/Fuera del algoritmo de la Figura 13/)).toBeInTheDocument();
    expect(screen.queryByText(/Hierro IV:/)).toBeNull();
  });

  it('Urgente: IST vacía → fuera del algoritmo', () => {
    render(<FeEpoUrgenteCalc />);
    set(/IST/, '');
    expect(screen.getByText(/Fuera del algoritmo de la Figura 13/)).toBeInTheDocument();
  });

  it('Urgente: IST < 20 mantiene la pauta de hoy (ferritina 60 → 500 mg + EPO 1 dosis)', () => {
    render(<FeEpoUrgenteCalc />);
    expect(screen.getByText('500 mg')).toBeInTheDocument();
    expect(screen.getByText(/dosis única/)).toBeInTheDocument();
  });
});
