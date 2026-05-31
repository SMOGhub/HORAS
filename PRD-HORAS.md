# HORAS — Product Requirements Document
**Version 1.0 — Mai 2026**

---

## Table des matières

1. [Identité produit](#1-identité-produit)
2. [Positionnement et promesse client](#2-positionnement-et-promesse-client)
3. [Personas utilisateurs](#3-personas-utilisateurs)
4. [Modules fonctionnels détaillés](#4-modules-fonctionnels-détaillés)
5. [Spécifications techniques](#5-spécifications-techniques)
6. [Modèle de tarification](#6-modèle-de-tarification)
7. [Roadmap de développement](#7-roadmap-de-développement)
8. [Stratégie d'accompagnement](#8-stratégie-daccompagnement)

---

## 1. Identité produit

### Nom : **HORAS**

*Du latin "horas" (les heures) — chaque heure compte sur un chantier.*
Acronyme possible : **H**ub **O**pérationnel pour les **R**essources, **A**ctivités et **S**uivi.

### Tagline
> *"Le logiciel qui travaille comme vous."*

### Vision produit
HORAS est la plateforme de gestion tout-en-un pensée pour les professionnels du bâtiment — des artisans indépendants aux PME de 100 personnes. Simple sur le terrain, puissant au bureau, transparent sur le contrat.

---

## 2. Positionnement et promesse client

### Problème central résolu
Les logiciels de gestion BTP existants souffrent de trois maux chroniques :
- **Tarification opaque** imposant des engagements annuels sans retour possible
- **Interfaces inadaptées au terrain** rendant l'outil inutilisable par les ouvriers
- **Performance insuffisante** sur les devis complexes et en mobilité

### Différenciation concurrentielle HORAS

| Axe | Concurrents (état de l'art) | HORAS |
|---|---|---|
| Prix | Sur devis, engagement annuel | Affiché, mensuel résiliable |
| Essai | Inexistant ou 7 jours avec CB | 30 jours, sans CB |
| Mobile | Application dégradée | Native offline-first |
| Terrain | Interface bureau adaptée | Interface dédiée ouvrier |
| Plans | Absent | Intégré avec annotation |
| Contrat | CGV défavorables | Droit de rétractation 14j garanti |

### Promesse client
> *"Essayez 30 jours sans engagement, sans carte bancaire. Restez parce que ça marche."*

---

## 3. Personas utilisateurs

### P1 — Le Dirigeant / Gérant
**Profil :** Marc, 44 ans, patron d'une entreprise de plomberie-chauffage, 8 salariés.
**Motivations :**
- Contrôler ses marges en temps réel sans passer des heures sur Excel
- Sortir des devis professionnels rapidement
- Avoir une vision globale de la trésorerie et du carnet de commandes

**Frustrations actuelles :**
- Logiciels trop chers avec engagements impossibles à rompre
- Données éparpillées entre logiciel de devis, comptable, Excel et post-its
- Mises à jour qui cassent ses habitudes sans prévenir

**Besoins clés dans HORAS :**
- Tableau de bord dirigeant avec KPIs en temps réel
- Alerte marge en dessous d'un seuil configurable
- Accès aux relances automatiques et au suivi de trésorerie

---

### P2 — Le Conducteur de Travaux
**Profil :** Sophie, 36 ans, conductrice de travaux dans une PME du gros œuvre, 25 personnes.
**Motivations :**
- Coordonner plusieurs chantiers simultanément
- Savoir qui est où, quand et pour combien d'heures
- Partager les plans et consignes avec les équipes terrain

**Frustrations actuelles :**
- Planning sur papier ou tableur non partagé en temps réel
- Impossibilité d'annoter les plans et les partager directement
- Rapports de chantier manuels perdus dans les e-mails

**Besoins clés dans HORAS :**
- Planning multi-chantiers par glisser-déposer
- Gestion et annotation des plans DWG/PDF
- Rapports journaliers depuis le terrain avec photos géolocalisées

---

### P3 — L'Ouvrier / Chef d'équipe terrain
**Profil :** Karim, 29 ans, chef d'équipe carreleur, peu à l'aise avec les outils numériques.
**Motivations :**
- Pointer ses heures simplement depuis son téléphone
- Consulter le bon de chantier et les plans du jour
- Signaler un problème ou prendre une photo sans appeler le bureau

**Frustrations actuelles :**
- Applications mobiles trop complexes, pensées pour les bureaux
- Perte de connexion sur les chantiers = outil inutilisable
- Obligation de tout saisir en fin de journée de mémoire

**Besoins clés dans HORAS :**
- Interface "terrain" ultra-simple : 3 actions max par écran
- Fonctionnement hors-ligne complet, synchronisation automatique
- Pointage en 2 taps (début/fin de chantier)

---

### P4 — La Secrétaire / Assistant(e) administratif(ve)
**Profil :** Nathalie, 52 ans, secrétaire polyvalente dans une entreprise de menuiserie, 12 personnes.
**Motivations :**
- Gérer les factures, acomptes et relances sans erreur
- Préparer les éléments pour le comptable facilement
- Ne pas être bloquée quand le logiciel change d'interface du jour au lendemain

**Frustrations actuelles :**
- Absence de gestion des factures d'acompte dans certains outils
- Relances manuelles chronophages et source d'oublis
- Mises à jour déstabilisantes sans documentation

**Besoins clés dans HORAS :**
- Gestion complète : devis → acompte → situation → solde
- Relances automatiques par e-mail/SMS configurables
- Exports comptables (FEC, intégration Sage, EBP, QuickBooks)

---

## 4. Modules fonctionnels détaillés

---

### 4.1 Gestion Commerciale

#### 4.1.1 Création de devis

**Bibliothèque d'ouvrages intelligente**
- Catalogue d'ouvrages composés (matériaux + main-d'œuvre + sous-traitance)
- Import/export depuis Batiprix, SEBTP, et catalogues personnalisés
- Recherche plein texte avec suggestions en cours de frappe
- Groupes et chapitres avec sous-totaux automatiques
- Options et variantes intégrées au devis (le client choisit)

**Assistant IA de rédaction**
- Dictée vocale : dicter les postes sur le chantier, l'IA structure le devis
- Suggestion automatique d'ouvrages liés ("si vous posez du carrelage, pensez à la colle, les joints, les plinthes")
- Reformulation automatique pour un rendu professionnel
- Détection des postes manquants basée sur le type de travaux décrit
- Génération de clauses contractuelles réglementaires (mentions légales, RGE, garanties)

**Performance sur devis complexes**
- Rendu virtuel (virtualisation de liste) : fluidité garantie jusqu'à 5 000 lignes
- Calcul de totaux en temps réel sans blocage de l'interface
- Sauvegarde automatique toutes les 30 secondes
- Mode "brouillon" pour travailler sans risque de perte

**Personnalisation du document**
- Templates visuels personnalisables (logo, couleurs, typographie)
- Mentions obligatoires pré-remplies selon l'activité (RGE, assurance décennale, etc.)
- Photos d'illustration intégrables dans le devis

#### 4.1.2 Signature électronique
- Signature en ligne conforme eIDAS (niveau avancé)
- Signature sur tablette en face-à-face client
- Relance automatique de signature à J+3, J+7, J+14
- Notification temps réel quand le client ouvre le devis
- Historique d'audit complet (timestamps, IP, actions)

#### 4.1.3 Facturation

**Types de documents supportés**
- Facture d'acompte (avec pourcentage ou montant fixe)
- Facture de situation (avancement chantier en %)
- Facture intermédiaire
- Facture de solde
- Avoir partiel ou total
- Facture récurrente (contrats de maintenance)

**Automatisations**
- Génération automatique de facture depuis le devis signé
- Relances automatiques configurables par client ou par catégorie :
  - J+30, J+45, J+60 après échéance
  - Ton modifiable : rappel courtois → lettre de mise en demeure
  - Canal configurable : e-mail et/ou SMS
- Lettrage automatique des paiements reçus (rapprochement bancaire)
- Export FEC mensuel pour le comptable

**Facturation électronique**
- Conformité Factur-X (norme française, obligatoire 2026)
- Connexion Chorus Pro pour les marchés publics
- Intégration portails clients grands comptes (Basware, Coupa)

---

### 4.2 Pilotage Financier

#### 4.2.1 Contrôle des marges en temps réel

**Vue par chantier**
- Marge prévisionnelle (depuis le devis)
- Marge réelle au fil de l'eau (heures pointées + achats saisis)
- Écart prévisionnel/réel avec code couleur (vert/orange/rouge)
- Alerte configurable : notification dirigeant si marge < seuil X%
- Courbe d'évolution de la marge dans le temps

**Vue globale entreprise**
- Tableau de bord avec chiffre d'affaires, marges, encours par période
- Comparaison N/N-1
- Top 5 chantiers les plus rentables / les moins rentables
- Prévision de trésorerie sur 3 mois glissants

#### 4.2.2 Achats et approvisionnement
- Bons de commande fournisseurs générés depuis les devis
- Réception de marchandises avec scan code-barres
- Affectation des achats à un chantier précis
- Comparateur de prix fournisseurs sur les références récurrentes

#### 4.2.3 Tableaux de bord personnalisables
- Widgets configurables par profil (dirigeant, conducteur de travaux)
- Export PDF automatique hebdomadaire/mensuel
- Partage sécurisé avec l'expert-comptable (accès lecture seule limité)

---

### 4.3 Gestion de Chantier

#### 4.3.1 Suivi opérationnel
- Fiche chantier centralisée : client, adresse, intervenants, documents
- Statut chantier : devis → accepté → planifié → en cours → réceptionné → soldé
- Journal de chantier journalier (météo, avancement, incidents)
- Indicateurs d'avancement en % configurable

#### 4.3.2 Rapports et comptes rendus
- Rapport journalier de chantier depuis mobile (photos + texte + heures)
- Modèles de rapport personnalisables
- Compte rendu de réunion de chantier avec suivi des actions
- Rapport de réception avec levée de réserves électronique
- Envoi automatique au client et à l'équipe par e-mail

#### 4.3.3 Gestion des photos
- Prise de photo directe depuis l'app mobile, affectée au chantier
- Géolocalisation et horodatage automatiques
- Organisation par album (avant travaux, pendant, après, réserves)
- Annotation sur photo (flèches, cercles, texte)
- Galerie partageable avec le client via lien sécurisé

#### 4.3.4 Gestion des plans — Module PLANS

**Visualisation**
- Visionneuse intégrée pour PDF, DWG (AutoCAD), DXF, IFC (BIM)
- Zoom fluide sans dégradation de qualité
- Navigation multi-pages et multi-niveaux

**Annotation collaborative**
- Outils d'annotation : flèches, formes, texte, pastilles numérotées
- Calques d'annotation par intervenant
- Historique des annotations avec nom et date
- Résolution de remarques (annotation fermée / ouverte)

**Partage terrain**
- Distribution des plans au personnel sur leur mobile
- Notification push lors d'une mise à jour de plan
- Plan en cache local (disponible hors-ligne)
- Version courante clairement identifiée (évite les doublons papier)

---

### 4.4 Gestion d'Équipe

#### 4.4.1 Planning
- Vue Gantt multi-chantiers, drag-and-drop
- Vue hebdomadaire par employé
- Gestion des absences (congés, maladie, formation) avec compteurs
- Conflits d'affectation détectés automatiquement
- Publication du planning avec notification aux équipes

#### 4.4.2 Pointage et suivi des heures
- Pointage mobile en 2 taps : début de chantier / fin de chantier
- Géofencing : validation automatique si l'employé est sur site
- Saisie manuelle avec validation chef d'équipe
- Heures supplémentaires, astreintes, déplacements
- Export vers logiciels de paie (Silae, Sage Paie, PayFit, ADP)

#### 4.4.3 Compétences et habilitations
- Fiche compétences par employé (CACES, habilitations électriques, etc.)
- Alertes de renouvellement (habilitation expirant dans 30/60/90 jours)
- Affectation intelligente : le planning suggère les employés qualifiés pour un type de chantier

#### 4.4.4 Notes de frais et déplacements
- Saisie des frais depuis mobile avec photo du justificatif
- Calcul automatique des indemnités kilométriques (barème fiscal)
- Validation workflow : employé → chef d'équipe → direction
- Intégration comptabilité (export N2F/Expensify compatible)

---

### 4.5 Application Mobile — Interface "Terrain"

#### Principe de conception
L'application mobile de HORAS est une application native (React Native) distincte de l'interface web. Elle est conçue selon le principe **"3 taps maximum"** : toute action courante doit être accessible en 3 interactions ou moins.

#### Architecture Offline-First
- Base de données locale SQLite synchronisée avec le serveur
- Toutes les actions réalisées hors-ligne sont mises en file d'attente
- Synchronisation automatique en arrière-plan dès retour de connexion
- Indicateur de statut de synchronisation visible en permanence
- Résolution de conflits automatique avec log consultable

#### Écran d'accueil personnalisé par rôle

**Vue Ouvrier**
```
[ MON CHANTIER DU JOUR ]
  Résidence Les Pins — Lot 3
  [ POINTER MON ARRIVÉE ]

[ MES TÂCHES ]
  ☐ Pose carrelage salle de bain (8h)
  ☐ Joint périphérique (1h)

[ PLANS DU CHANTIER ]   [ SIGNALER UN PROBLÈME ]
```

**Vue Chef d'équipe**
```
[ MON ÉQUIPE AUJOURD'HUI ]
  3/4 pointés ✓  |  Karim manquant ⚠

[ CHANTIERS EN COURS ]
  Résidence Les Pins     72% ●●●●○
  Maison Dupont          45% ●●○○○

[ RAPPORT JOURNALIER ] [ PHOTOS ] [ PLANNING ]
```

#### Fonctionnalités mobiles détaillées

| Fonctionnalité | Détail | Offline |
|---|---|---|
| Pointage | Début/fin, géolocalisation | ✓ |
| Consultation chantier | Fiche, tâches, contacts | ✓ |
| Rapport journalier | Texte + photos + heures | ✓ |
| Plans | Visualisation, annotation | ✓ (cache) |
| Notes de frais | Saisie + photo reçu | ✓ |
| Messagerie interne | Chat équipe par chantier | Partiel |
| Signature bon d'intervention | Sur tablette client | ✓ |
| Catalogue articles | Consultation prix | ✓ |
| Création devis simple | Pour petits travaux | ✓ |

#### Notifications push
- Planning du lendemain envoyé chaque soir à 18h
- Nouveau plan disponible sur un chantier affecté
- Tâche assignée ou modifiée
- Message de l'équipe ou du bureau
- Rappel de pointage si non effectué à 8h30

---

## 5. Spécifications Techniques

### 5.1 Stack technique recommandée

#### Frontend Web
- **Framework :** Next.js 15 (App Router) — SSR/SSG pour performance et SEO
- **UI :** Tailwind CSS + Radix UI (accessibilité native)
- **État global :** Zustand
- **Requêtes :** React Query (TanStack Query) avec cache intelligent
- **Tableaux haute performance :** TanStack Virtual (virtualisation de listes)
- **Plans/PDF :** PDF.js + Canvas API pour annotation

#### Application Mobile
- **Framework :** React Native (Expo SDK) — code partagé iOS/Android
- **Base de données locale :** WatermelonDB (SQLite, optimisé offline-first)
- **Synchronisation :** Architecture event-sourcing avec queue de synchronisation
- **Cartes/Géolocalisation :** Mapbox SDK

#### Backend
- **API :** Node.js / Fastify (performances supérieures à Express)
- **Base de données :** PostgreSQL 16 avec partitionnement par entreprise
- **Cache :** Redis pour sessions et données fréquentes
- **Files de messages :** BullMQ (relances, notifications, exports)
- **Recherche full-text :** Meilisearch (bibliothèque d'ouvrages)
- **Stockage fichiers :** S3-compatible (plans, photos, documents)

#### Infrastructure
- **Cloud :** AWS EU-West (Paris) — conformité RGPD souveraineté des données
- **CDN :** CloudFront pour assets et documents
- **Conteneurs :** Docker + Kubernetes (scalabilité automatique)
- **CI/CD :** GitHub Actions → tests → staging → production
- **Monitoring :** Sentry (erreurs) + Datadog (performance) + PagerDuty (alertes)

### 5.2 Performance — Objectifs et garanties

| Métrique | Objectif | Méthode |
|---|---|---|
| Chargement initial web | < 2s (LCP) | SSR + CDN + code splitting |
| Ouverture devis 500 lignes | < 500ms | Virtualisation de liste |
| Calcul totaux devis | Temps réel < 50ms | Web Worker dédié |
| API response time (P99) | < 200ms | Cache Redis + index DB |
| Mobile offline → sync | < 30s après reconnexion | Queue FIFO + delta sync |
| Uptime garanti | 99.9% (SLA) | Multi-AZ, health checks |

### 5.3 Sécurité

- **Authentification :** JWT + Refresh Token rotation, SSO SAML2/OIDC (Google, Microsoft)
- **MFA :** TOTP (Google Authenticator) et SMS pour toutes les formules Pro+
- **Chiffrement :** AES-256 at rest, TLS 1.3 in transit
- **Isolation des données :** Row-Level Security PostgreSQL — zéro fuite inter-tenant
- **RGPD :** Droit à l'export, droit à l'effacement, DPA fourni
- **Audit logs :** Toutes les actions sensibles (suppression, export, accès) tracées 1 an
- **Tests de sécurité :** Pentest annuel par tiers certifié, bug bounty program

### 5.4 API et Intégrations

#### API REST publique + webhooks
- Documentation OpenAPI 3.1 (Swagger UI)
- Versioning : `/api/v1/`, `/api/v2/` avec dépréciation 12 mois préavis
- Rate limiting par plan tarifaire
- SDK clients : JavaScript/TypeScript, Python (en priorité)

#### Intégrations natives incluses

**Comptabilité**
- Sage 50/100, EBP Compta, Ciel Compta
- QuickBooks Online, Pennylane, Indy
- Export FEC et grand livre

**Paie**
- Silae, PayFit, Sage Paie, ADP
- Export DSN-compatible

**Banque (Open Banking)**
- Bridge API / Powens — import relevés bancaires automatique
- Rapprochement bancaire semi-automatique

**Marketplaces BTP**
- BMCE Group / point.p, SEAC, Kiloutou (commandes fournisseurs)

**Communication**
- Twilio (SMS), Mailgun (e-mail transactionnel)
- Slack, Microsoft Teams (notifications)

**Signature électronique**
- Yousign (partenaire officiel, conforme eIDAS)

### 5.5 Politique de mises à jour

**Processus de déploiement**
1. Déploiement en environnement staging pendant 72h minimum
2. Tests automatisés (unit, integration, E2E avec Playwright)
3. Feature flags : activation progressive (5% → 20% → 100% des utilisateurs)
4. Note de version publiée AVANT le déploiement, visible dans l'app
5. Vidéo de 60s "Ce qui change" pour chaque évolution d'interface majeure
6. Ancien chemin de navigation conservé 30 jours en parallèle ("Nouveau / Ancien")

**Communication**
- In-app notification 7 jours avant toute modification d'interface
- Email récapitulatif mensuel des nouveautés
- Changelog public consultable à tout moment
- Accès au portail de votes et suggestions fonctionnelles

---

## 6. Modèle de Tarification

### Principes fondateurs
1. **Prix affichés publiquement**, sans "nous contacter"
2. **Sans engagement** : résiliation possible à tout moment, effet fin de mois
3. **30 jours d'essai gratuit**, sans carte bancaire
4. **Droit de rétractation légal** de 14 jours après tout achat, garanti contractuellement
5. **Pas de frais cachés** : onboarding, support, mises à jour inclus dans tous les plans

---

### Structure tarifaire

#### SOLO — 39€/mois HT
*Pour l'artisan indépendant ou l'auto-entrepreneur*

**Inclus :**
- 1 utilisateur
- Devis et factures illimités
- Bibliothèque d'ouvrages (500 items)
- Application mobile offline
- Signature électronique (10 documents/mois)
- Support par chat sous 24h (heures ouvrées)
- Stockage : 5 Go

---

#### ÉQUIPE — 89€/mois HT
*Pour les entreprises de 2 à 10 personnes*

**Tout SOLO, plus :**
- Jusqu'à 10 utilisateurs
- Module Chantier (rapports, photos, plans)
- Planning d'équipe et pointage
- Gestion des plans (visualisation + annotation)
- Relances automatiques clients
- Factures d'acompte et de situation
- Intégrations comptables (Sage, EBP, Pennylane)
- Module IA (dictée vocale, suggestions d'ouvrages)
- Signature électronique illimitée
- Stockage : 50 Go
- Support par chat sous 4h

---

#### ENTREPRISE — 189€/mois HT
*Pour les PME de 10 à 100 personnes*

**Tout ÉQUIPE, plus :**
- Utilisateurs illimités
- Multi-sites / multi-agences
- API complète + webhooks
- SSO (Google Workspace, Microsoft 365)
- MFA obligatoire configurable
- Rapports financiers avancés (consolidés multi-chantiers)
- Intégrations paie (Silae, PayFit, ADP)
- Open Banking (rapprochement bancaire)
- Gestion des habilitations et compétences
- Export FEC + accès comptable en lecture seule
- Stockage : 500 Go
- Support prioritaire < 1h (téléphone + chat)
- Onboarding dédié (4h de formation en visio)

---

#### GRAND COMPTE — Sur devis (à partir de 450€/mois HT)
*Pour les ETI, groupements et franchises*

**Tout ENTREPRISE, plus :**
- SLA personnalisé (jusqu'à 99.95%)
- Instance dédiée (isolation complète des données)
- Personnalisation de l'interface (white-label partiel)
- Intégrations métier sur mesure
- Customer Success Manager dédié
- Formation sur site
- Conformité SOC 2 Type II sur demande

---

### Tableau comparatif des plans

| Fonctionnalité | SOLO | ÉQUIPE | ENTREPRISE |
|---|:---:|:---:|:---:|
| Prix/mois HT | 39€ | 89€ | 189€ |
| Utilisateurs | 1 | 10 | Illimité |
| Devis / Factures | Illimité | Illimité | Illimité |
| App mobile offline | ✓ | ✓ | ✓ |
| Bibliothèque ouvrages | 500 | Illimité | Illimité |
| Gestion des plans | — | ✓ | ✓ |
| Pointage terrain | — | ✓ | ✓ |
| Module IA | — | ✓ | ✓ |
| API ouverte | — | — | ✓ |
| SSO / MFA | — | — | ✓ |
| Intégrations paie | — | — | ✓ |

### Remises
- **Annuel prépayé :** -15% (toujours résiliable, remboursement prorata)
- **Association/coopérative BTP :** -20% sur présentation
- **Parrainage :** 1 mois offert pour chaque filleul actif

---

## 7. Roadmap de développement

### Méthode de priorisation
Framework **RICE** (Reach × Impact × Confidence / Effort) appliqué à chaque fonctionnalité.

---

### Phase 0 — Fondations (Mois 1-3)

**Objectif :** MVP viable, capable d'acquérir les premiers clients payants.

**Technique :**
- Architecture multi-tenant PostgreSQL avec Row-Level Security
- Authentification JWT + OAuth2 (Google, Microsoft)
- CI/CD pipeline complet
- Infrastructure AWS EU-West, staging + production

**Produit (MVP) :**
- [ ] Gestion des clients et contacts
- [ ] Création de devis avec bibliothèque d'ouvrages basique
- [ ] Facturation (devis → facture → acompte)
- [ ] Interface web responsive (pas encore mobile natif)
- [ ] Relances e-mail automatiques
- [ ] Dashboard financier basique
- [ ] Onboarding guidé en 5 étapes
- [ ] Essai gratuit 30 jours auto-activé

**Cible Phase 0 :** 50 bêta-testeurs recrutés dans le réseau BTP

---

### Phase 1 — Cœur de valeur (Mois 4-6)

**Objectif :** Atteindre product-market fit, réduire le churn.

- [ ] Application mobile React Native (iOS + Android) — v1 online
- [ ] Pointage mobile avec géolocalisation
- [ ] Module Chantier : fiche, rapport journalier, photos
- [ ] Planning d'équipe (vue semaine)
- [ ] Signature électronique intégrée (Yousign)
- [ ] Intégrations comptables : Sage 50, EBP, Pennylane
- [ ] Performance devis : virtualisation de liste (objectif 500 lignes fluides)
- [ ] Feature flags system pour déploiements progressifs

**Cible Phase 1 :** 200 clients actifs, NPS > 45

---

### Phase 2 — Différenciation (Mois 7-9)

**Objectif :** Activer les fonctionnalités qui justifient l'upgrade ENTREPRISE.

- [ ] Architecture offline-first mobile (WatermelonDB)
- [ ] Gestion des plans : visionneuse PDF/DWG + annotation
- [ ] Module IA : dictée vocale → devis structuré
- [ ] Module IA : suggestions d'ouvrages liés
- [ ] Open Banking (import relevés, rapprochement)
- [ ] Gestion des habilitations et alertes renouvellement
- [ ] API publique v1 + documentation OpenAPI
- [ ] SSO SAML2 (Google Workspace, Microsoft 365)
- [ ] Conformité Factur-X (obligations légales 2026)

**Cible Phase 2 :** 500 clients, 20% sur plan ENTREPRISE

---

### Phase 3 — Scale (Mois 10-12)

**Objectif :** Préparer la croissance commerciale et les intégrations partenaires.

- [ ] Intégrations paie : Silae, PayFit
- [ ] Chorus Pro (marchés publics)
- [ ] Module IA avancé : détection de dérive de marge prédictive
- [ ] Marketplace intégrations (BMCE Group, Kiloutou)
- [ ] Multi-agences / consolidation groupe
- [ ] Application mobile v2 : création de devis offline
- [ ] Programme de parrainage in-app
- [ ] SDK JavaScript open source

**Cible Phase 3 :** 1 000 clients, 30 MRR

---

### Backlog futur (Post-an 1)

- BIM viewer (IFC) pour les chantiers tertiaires
- Intelligence artificielle prédictive sur les délais de chantier
- Place de marché sous-traitants (mise en relation)
- Module appels d'offres publics (scraping + analyse)
- Extension navigateur Chrome pour import depuis mails
- Intégration ChatGPT/Claude pour reformulation de CCTP

---

## 8. Stratégie d'accompagnement

### 8.1 Onboarding

**Objectif :** Amener un nouvel utilisateur à sa première valeur concrète en moins de 30 minutes.

**Parcours d'activation guidé**

```
Étape 1 (5 min) — Identité entreprise
  Nom, logo, informations légales, activité principale

Étape 2 (10 min) — Premier devis
  Création guidée avec 3 articles de la bibliothèque
  → Résultat : devis PDF professionnel téléchargeable

Étape 3 (5 min) — Inviter son équipe
  (optionnel, peut être passé)

Étape 4 (5 min) — Configurer les relances
  Activation des relances automatiques en 3 clics

Étape 5 — Découverte des modules
  Vidéos de 90s par module, accessibles à la demande
```

**Check-list de progression**
Barre de progression visible dans l'interface, avec petites récompenses (déblocage de templates premium) à chaque étape complétée.

**Webinaires d'onboarding**
- Session live chaque mardi à 12h (45 min) : "HORAS en pratique"
- Replay disponible dans le centre d'aide
- Session privée incluse dans le plan ENTREPRISE

---

### 8.2 Support client

**Canaux et délais par plan**

| Plan | Chat in-app | E-mail | Téléphone | Délai garanti |
|---|:---:|:---:|:---:|---|
| SOLO | ✓ | ✓ | — | 24h (jours ouvrés) |
| ÉQUIPE | ✓ | ✓ | — | 4h (jours ouvrés) |
| ENTREPRISE | ✓ | ✓ | ✓ | 1h (jours ouvrés) |
| GRAND COMPTE | ✓ | ✓ | ✓ CSM dédié | 30 min 24/7 |

**Centre d'aide**
- Base de connaissances avec recherche full-text (> 200 articles)
- Vidéos tutoriels indexées par module et par métier
- Guides PDF téléchargeables ("Le guide HORAS pour le plombier")
- Chatbot IA de première ligne (résout ~40% des tickets sans agent)

**Communauté utilisateurs**
- Forum modéré avec partage de bibliothèques d'ouvrages entre utilisateurs
- Votes pour les nouvelles fonctionnalités (roadmap publique)
- Programme beta-testeurs pour les clients ambassadeurs

---

### 8.3 Formation

**HORAS Academy** (inclus dans toutes les formules)
- Parcours certifiant "Maîtriser HORAS" : 4 modules × 1h
- Certificat PDF téléchargeable à l'issue (valorisable pour les dossiers qualité)
- Formation CPF-éligible (démarche QUALIOPI en cours)

**Formations sur mesure (payantes)**
- Formation équipe dirigeante (demi-journée en visio) : 350€ HT
- Formation terrain ouvriers (sur site) : 650€ HT/jour
- Formation comptabilité/facturation (2h en visio) : 200€ HT
- Pack ENTREPRISE : 4h de formation incluses

---

### 8.4 Conditions contractuelles — Charte éthique

**Ce que HORAS s'engage à ne jamais faire :**
- Imposer un engagement annuel sans option mensuelle
- Refuser le droit de rétractation légal de 14 jours
- Augmenter les prix en cours d'engagement sans préavis de 60 jours
- Bloquer l'export des données lors d'une résiliation
- Facturer les données après résiliation

**Ce que HORAS garantit contractuellement :**
- Résiliation à tout moment, effet fin de mois courant, sans pénalité
- Export complet de toutes vos données dans les 48h suivant une demande (JSON, CSV, PDF)
- Conservation de vos données 12 mois après résiliation (accès lecture seule)
- Préavis de 60 jours pour toute hausse tarifaire
- Prix bloqués 12 mois pour tout abonnement actif

**Tarifs affichés publiquement** sur la page pricing, sans "nous contacter", sans formulaire de capture préalable.

---

## Annexe A — Métriques de succès produit

### Acquisition
- Taux de conversion essai → payant : objectif > 25%
- Coût d'acquisition client (CAC) : < 3× MRR
- Délai essai → premier devis créé : < 48h

### Engagement
- Daily Active Users / Monthly Active Users : > 40%
- Taux de complétion onboarding : > 70%
- Nombre de devis créés par client actif/mois : > 5

### Rétention
- Churn mensuel : < 2%
- NPS (Net Promoter Score) : > 50
- CSAT support : > 4.5/5

### Croissance
- MRR Month-over-Month : > 15% (phase de croissance)
- Expansion revenue (upgrades) : > 20% du nouveau MRR

---

## Annexe B — Contraintes réglementaires BTP France

- Mentions obligatoires devis : n° SIREN, assurance décennale, garanties légales
- Facture électronique obligatoire B2B : 2026 (Factur-X)
- RGPD : traitement des données personnelles clients et salariés
- Conformité DSN : pour l'export des heures vers la paie
- RGE : gestion des certifications pour le suivi des travaux éligibles MaPrimeRénov'
- Signature électronique : conformité eIDAS niveau avancé

---

*Document rédigé par : Équipe Produit HORAS*
*Version : 1.0 — Mai 2026*
*Prochaine révision : Août 2026*
