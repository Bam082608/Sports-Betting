import React, { useState, useMemo } from 'react';
import {
  Shield,
  Target,
  Zap,
  TrendingUp,
  Grid,
  List,
  AlertTriangle,
  Activity,
  Clock,
  Lock
} from 'lucide-react';

const ReliabilityMatrix = () => {
  // CONFIGURATION
  const TARGET_SHOTS = 2; // Baseline for "Hit" calculation
  const MAX_TOI = 26; // Max minutes for progress bar scaling

  // MASTER DATA: AUDITED 12/05
  const [players] = useState([
    // --- TIER 1: THE IRONCLADS (Safe Volume) ---
    { id: 1, name: "Clayton Keller", team: "UTA", position: "RW", opponent: "VAN", last5: [3, 4, 4, 5, 4], odds: -450, goals: 9, assists: 14, toi_avg: 19.5, pp_avg: 3.5, ev_avg: 16.0, script_grade: "NEUTRAL" },
    { id: 2, name: "Jack Eichel", team: "VGK", position: "C", opponent: "NJD", last5: [2, 2, 7, 3, 5], odds: -590, goals: 8, assists: 22, toi_avg: 21.2, pp_avg: 3.8, ev_avg: 17.4, script_grade: "LOW PACE" },
    { id: 8, name: "Alex Ovechkin", team: "WSH", position: "LW", opponent: "ANA", last5: [4, 2, 2, 6, 3], odds: -620, goals: 15, assists: 10, toi_avg: 18.2, pp_avg: 4.1, ev_avg: 14.1, script_grade: "HISTORY CHASE" },
    { id: 3, name: "Dylan Guenther", team: "UTA", position: "RW", opponent: "VAN", last5: [5, 2, 3, 6, 3], odds: -500, goals: 12, assists: 9, toi_avg: 17.5, pp_avg: 3.2, ev_avg: 14.3, script_grade: "NEUTRAL" },

    // --- TIER 2: THE CHASE SQUAD (Buffalo Paradox) ---
    { id: 6, name: "Tage Thompson", team: "BUF", position: "C", opponent: "WPG", last5: [2, 4, 3, 2, 2], odds: -620, goals: 11, assists: 10, toi_avg: 18.8, pp_avg: 3.5, ev_avg: 15.3, script_grade: "CHASE MODE" },
    { id: 4, name: "Alex Tuch", team: "BUF", position: "RW", opponent: "WPG", last5: [2, 3, 4, 5, 2], odds: -196, goals: 9, assists: 13, toi_avg: 19.0, pp_avg: 2.5, ev_avg: 16.5, script_grade: "CHASE MODE" },
    { id: 14, name: "Jason Zucker", team: "BUF", position: "LW", opponent: "WPG", last5: [3, 2, 0, 4, 4], odds: -152, goals: 6, assists: 12, toi_avg: 14.5, pp_avg: 1.5, ev_avg: 13.0, script_grade: "CHASE MODE" },

    // --- TIER 3: SCRIPT RISKS ---
    { id: 70, name: "Jason Robertson", team: "DAL", position: "LW", opponent: "SJS", last5: [1, 2, 5, 2, 4], odds: -1300, goals: 8, assists: 12, toi_avg: 18.0, pp_avg: 3.0, ev_avg: 15.0, script_grade: "BLOWOUT RISK" },
    { id: 5, name: "Wyatt Johnston", team: "DAL", position: "C", opponent: "SJS", last5: [3, 2, 4, 2, 4], odds: -360, goals: 8, assists: 11, toi_avg: 18.5, pp_avg: 2.2, ev_avg: 16.3, script_grade: "BLOWOUT RISK" },

    // --- TIER 4: TACTICAL SUPPRESSION ---
    { id: 15, name: "Mikhail Sergachev", team: "UTA", position: "D", opponent: "VAN", last5: [1, 5, 1, 2, 4], odds: -140, goals: 4, assists: 12, toi_avg: 23.5, pp_avg: 3.0, ev_avg: 18.5, script_grade: "SUPPRESSED" },

    // --- TIER 5: HIDDEN GEMS ---
    { id: 9, name: "Kyle Connor", team: "WPG", position: "LW", opponent: "BUF", last5: [4, 2, 3, 1, 2], odds: -620, goals: 14, assists: 16, toi_avg: 20.5, pp_avg: 3.8, ev_avg: 16.7, script_grade: "NEUTRAL" },
    { id: 16, name: "Dawson Mercer", team: "NJD", position: "C", opponent: "VGK", last5: [3, 5, 3, 2, 1], odds: -154, goals: 5, assists: 7, toi_avg: 16.5, pp_avg: 1.5, ev_avg: 14.0, script_grade: "LOW PACE" },
  ]);

  const [viewMode, setViewMode] = useState('list');

  // ENGINE: Process stats and assign visual flags
  const analyzedPlayers = useMemo(() => {
    return players.map(p => {
      // Hit Rate
      const hits = p.last5.filter(s => s >= TARGET_SHOTS).length;

      // Shooter Ratio: Does he shoot (Goal) or Pass (Assist)?
      // If Goals > 60% of Assists, he's a pure shooter.
      const isShooter = p.goals > (p.assists * 0.6);

      // Deployment Math
      const totalWidth = Math.min((p.toi_avg / MAX_TOI) * 100, 100);
      const evPercent = (p.ev_avg / p.toi_avg) * 100;
      const ppPercent = (p.pp_avg / p.toi_avg) * 100;

      return { ...p, hits, isShooter, totalWidth, evPercent, ppPercent };
    }).sort((a, b) => {
      // Sorting Priority: Chase Mode -> High Hits -> TOI
      if (a.script_grade === "CHASE MODE" && b.script_grade !== "CHASE MODE") return -1;
      if (b.script_grade === "CHASE MODE" && a.script_grade !== "CHASE MODE") return 1;
      return b.hits - a.hits || b.toi_avg - a.toi_avg;
    });
  }, [players]);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-200 p-2 font-sans pb-20">

      {/* --- DASHBOARD HEADER --- */}
      <div className="sticky top-0 bg-slate-950/95 backdrop-blur z-20 pb-4 pt-2 border-b border-slate-800 mb-4 shadow-xl">
        <div className="flex justify-between items-center px-2">
          <div>
            <h1 className="text-xl font-bold text-emerald-500 tracking-tighter flex items-center gap-2">
              <Shield className="w-5 h-5" /> RELIABILITY<span className="text-white">MATRIX</span>
              <span className="text-[10px] text-slate-500 font-normal border border-slate-800 px-1 rounded">v9.0</span>
            </h1>
            <p className="text-[10px] text-slate-500 uppercase tracking-widest mt-1 pl-1">
              Operation Dec 5 • <span className="text-emerald-500 animate-pulse">Live</span>
            </p>
          </div>
          <button
            onClick={() => setViewMode(viewMode === 'list' ? 'grid' : 'list')}
            className="p-2 bg-slate-900 rounded border border-slate-800 text-slate-400 hover:text-white transition-colors"
          >
             {viewMode === 'list' ? <Grid size={18}/> : <List size={18}/>}
          </button>
        </div>
      </div>

      {/* --- PLAYER GRID/LIST --- */}
      <div className={viewMode === 'grid' ? "grid grid-cols-1 sm:grid-cols-2 gap-3" : "flex flex-col gap-3"}>
        {analyzedPlayers.map((p, index) => {

          // DYNAMIC STYLING BASED ON INTELLIGENCE
          let borderColor = "border-slate-800";
          let shadowColor = "";
          let scriptBadgeColor = "bg-slate-800 text-slate-500 border-slate-700";

          if (p.script_grade === "CHASE MODE") {
            borderColor = "border-emerald-500";
            shadowColor = "shadow-[0_0_15px_-5px_rgba(16,185,129,0.3)]";
            scriptBadgeColor = "bg-emerald-950 text-emerald-400 border-emerald-500/50";
          } else if (p.script_grade === "BLOWOUT RISK") {
            borderColor = "border-amber-500/50";
            scriptBadgeColor = "bg-amber-950 text-amber-500 border-amber-500/50";
          } else if (p.script_grade === "SUPPRESSED") {
            borderColor = "border-red-900/50";
            scriptBadgeColor = "bg-red-950 text-red-500 border-red-500/50";
          } else if (p.script_grade === "HISTORY CHASE") {
            borderColor = "border-purple-500/50";
            scriptBadgeColor = "bg-purple-950 text-purple-400 border-purple-500/50";
          }

          return (
            <div
              key={p.id}
              className={`relative bg-slate-900 rounded-lg p-3 border ${borderColor} ${shadowColor} transition-all hover:bg-slate-850`}
            >

              {/* RANKING ORBIT */}
              <div className="absolute -left-2 -top-2 w-6 h-6 bg-slate-950 border border-slate-700 rounded-full flex items-center justify-center text-[10px] font-black text-slate-400 z-10">
                {index + 1}
              </div>

              {/* INTELLIGENCE BADGE */}
              <div className={`absolute right-2 top-2 px-1.5 py-0.5 rounded text-[8px] font-bold uppercase tracking-wider border flex items-center gap-1 ${scriptBadgeColor}`}>
                {p.script_grade === "SUPPRESSED" ? <Lock size={8} /> : <Activity size={8} />}
                {p.script_grade}
              </div>

              {/* IDENTITY BLOCK */}
              <div className="flex items-center gap-3 mb-3 pl-2 mt-1">
                 <div className="w-10 h-10 rounded bg-slate-800 flex items-center justify-center font-bold text-sm border border-slate-700 text-slate-300">
                    {p.team}
                 </div>
                 <div>
                    <div className="font-bold text-sm text-white flex items-center gap-2">
                      {p.name}
                      {p.isShooter && <Zap size={10} className="text-yellow-400 fill-yellow-400" />}
                    </div>
                    <div className="text-[10px] text-slate-400 flex gap-2">
                      <span>{p.position}</span>
                      <span className="text-slate-600">•</span>
                      <span>vs {p.opponent}</span>
                    </div>
                 </div>
              </div>

              {/* DEPLOYMENT VISUALIZER */}
              <div className="mt-2 mb-3 px-1 bg-slate-950/50 p-2 rounded border border-slate-800/50">
                <div className="flex justify-between text-[9px] mb-1.5 text-slate-400 uppercase tracking-wider font-semibold">
                  <span className="flex items-center gap-1"><Clock size={8}/> TOI: {p.toi_avg}m</span>
                  <div className="flex gap-2">
                    <span className="text-emerald-500">EV {p.ev_avg}</span>
                    <span className="text-blue-400">PP {p.pp_avg}</span>
                  </div>
                </div>

                {/* THE BAR */}
                <div className="h-2.5 w-full bg-slate-900 rounded-sm overflow-hidden flex relative border border-slate-800">
                   <div className="h-full flex" style={{ width: `${p.totalWidth}%` }}>
                      {/* Even Strength Segment */}
                      <div className="h-full bg-emerald-600/80" style={{ width: `${p.evPercent}%` }}></div>
                      {/* Power Play Segment */}
                      <div className="h-full bg-blue-500/80" style={{ width: `${p.ppPercent}%` }}></div>
                   </div>
                </div>
              </div>

              {/* TREND LINE & HIT RATE */}
              <div className="flex justify-between items-end mt-2 pt-2 border-t border-slate-800/50">
                <div className="flex flex-col gap-1">
                  <span className="text-[8px] uppercase text-slate-600 font-bold tracking-widest">Last 5 Games</span>
                  <div className="flex gap-1">
                    {p.last5.map((shots, i) => (
                      <div
                        key={i}
                        className={`w-2 h-6 rounded-sm flex items-end justify-center ${shots >= TARGET_SHOTS ? 'bg-emerald-500' : 'bg-slate-800 border border-slate-700'}`}
                      >
                         <span className="text-[7px] font-bold text-slate-950 mb-0.5">{shots}</span>
                      </div>
                    ))}
                  </div>
                </div>

                <div className="text-right">
                    <div className="text-[9px] text-slate-500 mb-0.5">Implied Odds</div>
                    <div className={`font-mono text-xs font-bold ${p.script_grade === 'CHASE MODE' ? 'text-emerald-400' : 'text-slate-300'}`}>
                      {p.odds}
                    </div>
                </div>
              </div>

            </div>
          );
        })}
      </div>
    </div>
  );
};

export default ReliabilityMatrix;
