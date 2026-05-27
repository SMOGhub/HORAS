# Product Requirements Document — BATISYNC

**Version :** 1.0  
**Date :** 2026-05-27  
**Statut :** Draft  
**Auteur :** Product Owner — Division SaaS BTP

---

## Table des matières

1. [Nom, positionnement et promesse client](#1-nom-positionnement-et-promesse-client)
2. [Personas utilisateurs](#2-personas-utilisateurs)
3. [Modules fonctionnels détaillés](#3-modules-fonctionnels-détaillés)
4. [Spécificités techniques](#4-spécificités-techniques)
5. [Modèle de tarification transparent](#5-modèle-de-tarification-transparent)
6. [Roadmap de développement priorisée](#6-roadmap-de-développement-priorisée)
7. [Stratégie d'accompagnement](#7-stratégie-daccompagnement)

---

## 1. Nom, positionnement et promesse client

### 1.1 Nom du produit

**BATISYNC**

- **Bati** : ancrage métier immédiat (bâtiment)
- **Sync** : synchronisation des données, des équipes, du terrain au bureau
- Disponible en `.io`, `.fr`, `.com`
- Mémorisable, prononçable dans tous les corps de métier

### 1.2 Positionnement

BATISYNC est le logiciel de gestion tout-en-un pour les professionnels du bâtiment : artisans indépendants, TPE et PME jusqu'à 150 collaborateurs. Il couvre l'intégralité du cycle de vie d'un chantier, du devis à la clôture financière, avec une application mobile native fonctionnant hors connexion.

**Différenciation concurrentielle :**

| Axe | Concurrents (Vertuoza, etc.) | BATISYNC |
|---|---|---|
| Tarification | Opaque, sur devis uniquement | Publique, 3 paliers clairs |
| Essai | Absent ou limité | 30 jours gratuits, sans CB |
| Mobile | Obsolète, pas d'offline | Native iOS/Android, 100 % offline |
| Interface terrain | Inadaptée aux ouvriers | UI dédiée, simplifiée, tactile |
| Plans | Non géré | Visionneuse annotable intégrée |
| Facturation | Partielle (pas d'acomptes) | Cycle complet avec relances auto |
| Contrat | Engagement annuel rigide | Mensuel sans engagement, résiliation 1 clic |
| Performance | Lente sur devis longs | Virtualisation des listes, <100 ms |

### 1.3 Promesse client

> *"Du devis signé au chantier livré, BATISYNC tient vos marges, vos équipes et vos clients — depuis n'importe où, même sans réseau."*

---

## 2. Personas utilisateurs

### 2.1 Persona A — Le Dirigeant / Artisan patron

**Prénom fictif :** Marc, 42 ans  
**Contexte :** Gérant d'une entreprise de plomberie-chauffage de 8 personnes. Passe 40 % de son temps en déplacement, fait lui-même ses devis le soir.

**Besoins prioritaires :**
- Créer un devis depuis son téléphone en 10 minutes
- Connaître la marge réelle de chaque chantier en temps réel
- Envoyer une facture et recevoir un paiement en ligne

**Frustrations actuelles :**
- Tarif opaque ; a dû appeler 3 fois avant d'avoir un prix
- Pas pu essayer avant de signer ; a perdu de l'argent
- Application mobile trop lente pour être utilisable sur chantier

**KPI de succès :** Temps de création d'un devis < 15 min ; délai de paiement client réduit de 30 %

---

### 2.2 Persona B — Le Conducteur de travaux

**Prénom fictif :** Sophie, 35 ans  
**Contexte :** Conductrice de travaux dans une PME de 45 salariés (menuiserie / aménagement). Gère 8 à 12 chantiers simultanément.

**Besoins prioritaires :**
- Suivre l'avancement de chaque chantier sur un seul écran
- Valider les heures de ses équipes terrain
- Annoter des plans et les partager instantanément

**Frustrations actuelles :**
- Interface chef de chantier peu intuitive
- Impossibilité d'annoter les plans dans l'outil ; retour aux emails et PDF
- Mises à jour qui changent l'interface sans prévenir

**KPI de succès :** Réduction des réunions de coordination de 25 % ; zéro plan imprimé sur chantier

---

### 2.3 Persona C — L'Ouvrier / Technicien terrain

**Prénom fictif :** Karim, 28 ans  
**Contexte :** Électricien qualifié. Peu à l'aise avec les outils numériques ; utilise un smartphone Android milieu de gamme.

**Besoins prioritaires :**
- Pointer ses heures sans effort (< 30 secondes)
- Consulter le plan du chantier sur téléphone
- Envoyer une photo de fin de chantier avec commentaire

**Frustrations actuelles :**
- Interface incompréhensible, trop de menus
- Application lente sur son téléphone
- Perd la connexion réseau dans les caves et sous-sols

**KPI de succès :** Taux d'adoption terrain > 90 % en 30 jours ; zéro pointage papier

---

### 2.4 Persona D — L'Assistante administrative / Comptable

**Prénom fictif :** Nathalie, 48 ans  
**Contexte :** Secrétaire comptable dans une entreprise de maçonnerie de 20 personnes. Gère facturation, relances et export comptable.

**Besoins prioritaires :**
- Gérer les factures d'acompte, les situations de travaux et la facture finale
- Lancer des relances automatiques sans intervention manuelle
- Exporter les écritures comptables vers Sage ou EBP en 1 clic

**Frustrations actuelles :**
- Pas de facture d'acompte dans l'outil actuel
- Relances manuelles chronophages
- Export comptable inexistant ou incomplet

**KPI de succès :** Réduction du temps de facturation de 50 % ; taux de recouvrement < 60 jours amélioré de 20 %

---

## 3. Modules fonctionnels détaillés

### 3.1 Module Gestion Commerciale

#### 3.1.1 Création de devis

**Bibliothèque d'ouvrages intelligente**
- Base de données d'ouvrages structurés : main-d'œuvre + fournitures + sous-traitance par ouvrage
- Import depuis les bases BATIPRIX, UNTEC, ou catalogue propre
- Composition automatique : sélection d'un ouvrage tire toutes les lignes associées
- Recherche full-text instantanée (< 50 ms) avec suggestions IA

**Performance sur devis complexes**
- Virtualisation de liste (rendu DOM partiel) : fluidité garantie jusqu'à 2 000 lignes
- Sauvegarde automatique toutes les 30 secondes
- Mode "brouillon hors ligne" : continuer à éditer sans réseau, sync à la reconnexion

**Dictée vocale et IA**
- Dictée vocale native (iOS/Android + Web Speech API)
- Assistant IA de rédaction : génère une description professionnelle à partir de mots-clés métier
- Suggestion de prix : IA propose un tarif basé sur l'historique des devis de l'entreprise
- Détection d'incohérence : alerte si le prix unitaire s'écarte de plus de 30 % de la moyenne historique

**Collaboration**
- Devis multi-versions avec historique des modifications
- Commentaires internes par ligne
- Attribution à un commercial ou conducteur de travaux

#### 3.1.2 Envoi et signature électronique

- Envoi par email avec lien de consultation sécurisé (token unique)
- Portail client : le client visualise, pose des questions, accepte ou refuse
- Signature électronique conforme eIDAS niveau simple (intégration DocuSign ou solution native)
- Notification temps réel (push / email) : "Votre devis a été ouvert", "Votre devis a été signé"
- Signature depuis mobile client sans installation d'application

#### 3.1.3 Cycle de facturation complet

**Types de documents**
- Devis → Commande → Facture d'acompte → Situation de travaux → Facture finale → Avoir
- Génération automatique depuis le devis accepté (zéro ressaisie)

**Facture d'acompte**
- Pourcentage ou montant fixe
- TVA correctement ventilée
- Imputation automatique sur la facture finale

**Situations de travaux**
- Avancement par ligne ou par poste (%)
- Cumul des situations précédentes
- Génération du solde restant dû automatique

**Paiement en ligne**
- Lien de paiement Stripe ou GoCardless intégré dans la facture
- Paiement par carte, virement SEPA ou prélèvement
- Rapprochement automatique encaissement / facture

**Relances automatiques**
- Scénarios configurables : J+15 email doux → J+30 email ferme → J+45 courrier recommandé virtuel
- Personnalisation par client (certains clients en exclusion)
- Tableau de bord des impayés avec vieillissement de créances

---

### 3.2 Module Pilotage Financier

#### 3.2.1 Suivi de rentabilité par chantier

- Marge brute et marge nette en temps réel par chantier
- Comparaison prévu / réalisé : heures, matériaux, sous-traitance
- Alerte automatique si la marge descend sous un seuil configurable (ex. : < 20 %)
- Drill-down par poste : voir exactement quelle ligne dévore la marge

#### 3.2.2 Tableaux de bord direction

**Vue globale**
- Chiffre d'affaires mensuel vs objectif
- Backlog signé (devis acceptés non encore facturés)
- DSO (Days Sales Outstanding) — délai moyen de règlement
- Top 5 chantiers les plus rentables / les moins rentables

**Graphiques interactifs**
- Courbe de CA sur 12 mois glissants
- Histogramme marges par corps de métier
- Carte de chaleur des chantiers actifs (intégration carte)

**Export**
- Export PDF pour présentation banque / expert-comptable
- Export Excel / CSV pour analyse personnalisée
- Connexion directe API vers Pennylane, Sage 50, EBP Bâtiment, QuickBooks

#### 3.2.3 Gestion des achats et fournisseurs

- Bons de commande fournisseurs depuis les lignes de devis
- Réception partielle ou totale avec mise à jour automatique du stock chantier
- Comparaison devis fournisseur vs prix réel livré
- Catalogue fournisseurs avec tarifs négociés (prix remisés)

---

### 3.3 Module Gestion de Chantier

#### 3.3.1 Tableau de bord chantiers

- Liste des chantiers avec statut visuel (En préparation / En cours / En attente / Livré / Clôturé)
- Vue Kanban ou liste configurable
- Filtres : conducteur de travaux, corps de métier, date de livraison prévue
- Indicateurs par chantier : avancement (%), jours restants, budget consommé

#### 3.3.2 Journal de chantier

- Entrées quotidiennes : météo automatique (API géolocalisation), effectifs présents, tâches réalisées
- Photos géolocalisées et horodatées depuis l'application mobile
- Rapport journalier généré automatiquement (PDF) et envoyable au client
- Incidents et réserves : signalement avec photo, assignation, suivi de résolution

#### 3.3.3 Gestion des plans

**Visionneuse intégrée**
- Formats supportés : PDF, DWG (viewer), PNG, JPG, IFC (viewer 3D basique)
- Zoom fluide, rotation, couches activables/désactivables

**Annotation collaborative**
- Outils : flèche, texte, zone, pin géolocalisé sur le plan
- Annotations avec auteur, date et statut (ouvert / résolu)
- Notifications push aux équipes concernées par une annotation

**Partage terrain**
- Accès depuis l'application mobile en mode hors ligne (plans téléchargés à l'avance)
- Version des plans : l'ancienne version est archivée, la nouvelle est notifiée aux équipes
- Contrôle d'accès : certains plans accessibles uniquement à certains rôles

#### 3.3.4 Gestion des documents chantier

- GED (Gestion Électronique de Documents) par chantier
- Dossier automatique : PPSPS, DOE, PV de réception, garanties
- Signature électronique du PV de réception par le client sur tablette
- Archivage légal 10 ans conforme

---

### 3.4 Module Gestion d'Équipe

#### 3.4.1 Planning

**Vue planning**
- Gantt interactif par chantier (drag & drop des tâches)
- Vue hebdomadaire par collaborateur (charge de travail)
- Détection des conflits : alerte si un collaborateur est affecté à deux chantiers simultanément

**Gestion des absences**
- Congés, RTT, arrêts maladie, formation
- Intégration avec le pointage (les jours d'absence sont déduits automatiquement)
- Soldes de congés en temps réel

#### 3.4.2 Pointage

**Méthodes de pointage (configurables par entreprise)**
- Pointage GPS : le salarié doit être dans un rayon défini autour du chantier
- QR Code chantier : scan à l'entrée et à la sortie
- NFC (badge) : pour les entreprises équipées
- Manuel avec validation chef de chantier : saisie libre + validation hiérarchique

**Traitement des heures**
- Différenciation heures normales / heures supplémentaires / heures de nuit / paniers
- Export DSN-ready pour les logiciels de paie (SILAE, PayFit, ADP)
- Résumé hebdomadaire envoyé au salarié par email

#### 3.4.3 Compétences et habilitations

- Fiche compétences par collaborateur (CACES, habilitations électriques, SST, etc.)
- Alertes automatiques avant expiration d'une habilitation (J-60, J-30, J-0)
- Affectation intelligente : le planning propose les collaborateurs ayant les compétences requises

---

### 3.5 Application Mobile

#### 3.5.1 Deux interfaces distinctes

**Interface "Direction / Bureau"** (identique au web, responsive)
- Accès complet à tous les modules
- Idéal pour dirigeant et conducteur de travaux en déplacement
- Synchronisation temps réel

**Interface "Terrain"** (simplifiée, pensée pour l'ouvrier)
- 4 actions visibles sur l'écran d'accueil :
  1. **Pointer** (arrivée / départ — 1 tap)
  2. **Mon chantier** (plan + tâches du jour)
  3. **Photo** (prendre et envoyer une photo avec commentaire vocal)
  4. **Rapport** (remplir le rapport journalier — checklist guidée)
- Polices et boutons surdimensionnés (accessibilité, gants de travail)
- Pas de menu complexe, pas de notion de "module"

#### 3.5.2 Mode hors ligne

**Architecture offline-first**
- Base de données locale SQLite / Realm synchronisée avec le serveur
- Toutes les données du chantier actif sont téléchargées à l'avance (plans inclus)
- Les actions effectuées hors ligne sont mises en file d'attente et synchronisées dès la reconnexion
- Indicateur visuel permanent : "En ligne" / "Hors ligne — X actions en attente"

**Gestion des conflits**
- Stratégie "last-write-wins" pour les pointages
- Stratégie "merge manuel" pour les annotations de plans (notification à l'auteur)
- Aucune perte de données garantie : toute action est loggée localement avant d'être envoyée

#### 3.5.3 Notifications push

- Devis signé par un client
- Facture impayée atteignant le délai de relance
- Habilitation d'un collaborateur proche de l'expiration
- Nouveau plan ou nouvelle version de plan disponible
- Message direct depuis un conducteur de travaux

---

## 4. Spécificités techniques

### 4.1 Stack technique

**Frontend Web**
- Framework : **React 18** avec **TypeScript strict**
- State management : **Zustand** (léger) + **React Query** pour le cache serveur
- Rendu des listes longues : **TanStack Virtual** (virtualisation DOM — clé de performance devis complexes)
- Design system : composants sur mesure basés sur **Radix UI** + **Tailwind CSS**
- Bundler : **Vite** (build < 3 s en dev)

**Frontend Mobile**
- Framework : **React Native** (iOS + Android depuis une base commune)
- Navigation : **Expo Router**
- Stockage local offline : **WatermelonDB** (base relationnelle locale, haute performance)
- Sync offline : file d'attente persistante avec **react-native-queue**

**Backend**
- Runtime : **Node.js 22** avec **Fastify** (3× plus rapide qu'Express)
- API : **GraphQL** (Apollo Server) pour les requêtes complexes + **REST** pour les webhooks et intégrations tierces
- ORM : **Prisma** avec migrations versionnées
- Base de données principale : **PostgreSQL 16** (JSONB pour les structures flexibles de devis)
- Cache : **Redis** (sessions, rate-limiting, invalidation de cache)
- Temps réel : **WebSocket** via **Socket.io** (notifications live, collaboration)

**Infrastructure**
- Cloud : **AWS** (region eu-west-3 Paris — conformité RGPD)
- Conteneurs : **Docker** + orchestration **ECS Fargate** (auto-scaling sans gestion de serveurs)
- CDN : **CloudFront** (assets statiques < 50 ms partout en Europe)
- Stockage fichiers : **S3** avec chiffrement at-rest (plans, photos, documents)
- CI/CD : **GitHub Actions** → tests → staging → production (déploiement blue/green)

### 4.2 Performance et fiabilité

**Objectifs SLA**
- Disponibilité : 99,9 % (< 9 heures d'indisponibilité par an)
- Temps de réponse API : P95 < 200 ms, P99 < 500 ms
- Chargement initial application : < 2 s (réseau 4G)
- Rendu d'un devis de 500 lignes : < 100 ms (virtualisation)

**Tests de charge**
- Cibles : 10 000 utilisateurs simultanés dès la V1
- Tests Locust automatisés dans la pipeline CI sur chaque release

### 4.3 Sécurité

- Authentification : **OAuth2 / OIDC** avec support SSO (Google Workspace, Microsoft 365)
- MFA obligatoire pour les rôles direction et comptabilité
- Chiffrement en transit : TLS 1.3
- Chiffrement au repos : AES-256 (S3 + RDS)
- Audit log : chaque action sensible (suppression, export, accès document) est tracée
- RGPD : droit à l'effacement, export des données, DPA disponible
- Tests de pénétration annuels par prestataire tiers certifié

### 4.4 API ouverte et intégrations

**API REST publique**
- Documentation OpenAPI 3.1 interactive (Swagger UI)
- Versioning : `/api/v1/`, `/api/v2/` — support de l'ancienne version pendant 12 mois minimum
- Rate limiting : 1 000 req/min par clé API (configurable sur demande)
- Webhooks : événements déclenchables (devis signé, facture émise, pointage créé, etc.)

**Intégrations natives (V1)**
- **Comptabilité :** Pennylane, Sage 50, EBP Bâtiment, Cegid, QuickBooks
- **Paie :** SILAE, PayFit, ADP Decidium
- **Stockage :** Google Drive, Microsoft SharePoint, Dropbox
- **Communication :** Slack, Microsoft Teams (notifications projet)
- **Paiement :** Stripe, GoCardless

**Intégrations V2 (roadmap)**
- Places de marché matériaux : POINT.P Connect, Manutan Pro
- Logiciels BIM : Autodesk BIM 360, Procore
- BI : Power BI, Tableau (connecteur natif)

### 4.5 Politique de mise à jour

- **Déploiements blue/green** : 0 interruption de service
- **Feature flags** : chaque nouvelle fonctionnalité est activable progressivement (5 % → 20 % → 100 % des utilisateurs)
- **Release notes** : notification in-app avant chaque déploiement majeur avec tutoriel interactif ("Voici ce qui change")
- **Rollback automatique** : si le taux d'erreur dépasse 1 % après un déploiement, retour automatique à la version précédente en < 5 min
- **Changelog public** : page `/changelog` mise à jour à chaque release, accessible sans connexion

---

## 5. Modèle de tarification transparent

### 5.1 Principes fondateurs

1. **Prix affichés publiquement** sur le site — aucun "tarif sur devis"
2. **Sans engagement** — résiliation possible à tout moment, 1 mois de préavis
3. **Essai gratuit 30 jours** — sans carte bancaire, accès complet
4. **Données exportables** à tout moment, même lors de la résiliation
5. **Remboursement pro-rata** en cas de résiliation en cours de mois

### 5.2 Grille tarifaire

#### Formule STARTER — 49 €/mois HT

*Pour l'artisan indépendant ou la micro-entreprise*

- 1 utilisateur
- Devis et factures illimités
- Bibliothèque d'ouvrages (500 ouvrages)
- Application mobile (interface terrain)
- Signature électronique (10 signatures/mois)
- Support par email (réponse sous 24h)

---

#### Formule CHANTIER — 129 €/mois HT

*Pour les TPE de 2 à 10 personnes*

- Jusqu'à 10 utilisateurs
- Tout STARTER +
- Pilotage financier complet (marges, tableaux de bord)
- Gestion des plans (visionneuse + annotations)
- Pointage équipe (GPS + QR Code)
- Journal de chantier et rapports journaliers
- Intégrations comptables (Pennylane, Sage, EBP)
- Signature électronique illimitée
- Support chat (réponse sous 4h)

---

#### Formule ENTREPRISE — 299 €/mois HT

*Pour les PME de 10 à 150 personnes*

- Utilisateurs illimités
- Tout CHANTIER +
- SSO (Google / Microsoft)
- API ouverte + webhooks
- Intégrations paie (SILAE, PayFit)
- Gestionnaire de compte dédié
- Onboarding personnalisé (2 sessions de formation)
- SLA 99,9 % garanti contractuellement
- Support téléphonique prioritaire (réponse < 1h)

---

#### Options à la carte (tous plans)

| Option | Prix |
|---|---|
| Utilisateur supplémentaire (STARTER) | 15 €/mois/user |
| Signature électronique supplémentaire | 0,50 €/signature |
| Archivage documents 10 ans | 9 €/mois |
| Formation vidéo premium | Incluse (bibliothèque en ligne) |
| Formation présentielle (demi-journée) | 490 € HT |

### 5.3 Conditions contractuelles conformes

- **Droit de rétractation** : 14 jours légaux après la souscription, remboursement intégral sans justification
- **Résiliation** : formulaire en ligne, 1 mois de préavis, aucune pénalité
- **Export des données** : disponible dans les 30 jours suivant la résiliation (formats CSV, JSON, PDF)
- **Suppression des données** : conformément au RGPD, sous 90 jours après fin de contrat
- Les CGU sont rédigées en français courant, sans jargon juridique opaque

---

## 6. Roadmap de développement priorisée

### Méthode de priorisation

Scoring MoSCoW adapté : impact métier × fréquence d'usage × complexité de développement

---

### Phase 0 — Fondations (Mois 1–2)

**Objectif :** Infrastructure, authentification, CI/CD opérationnels

- [ ] Setup infra AWS (VPC, ECS, RDS, S3, CloudFront)
- [ ] Authentification OAuth2 + MFA
- [ ] Design system (composants de base, Storybook)
- [ ] Pipeline CI/CD GitHub Actions
- [ ] Environnements : dev / staging / production
- [ ] Monitoring : Sentry (erreurs), Datadog (perf), Grafana (infra)

---

### Phase 1 — MVP Commercial (Mois 3–5)

**Objectif :** Permettre à un artisan de créer un devis et une facture

- [ ] Module Devis : création, bibliothèque d'ouvrages, calcul automatique
- [ ] Module Facturation : facture simple, acompte, avoir
- [ ] Signature électronique (DocuSign ou Universign)
- [ ] Portail client (lien de consultation + validation devis)
- [ ] Paiement en ligne (Stripe)
- [ ] PDF générés (devis + facture aux couleurs de l'entreprise)
- [ ] Application mobile — Interface Terrain (pointage + photo)
- [ ] Mode hors ligne mobile (WatermelonDB + sync queue)
- [ ] Onboarding guidé (checklist 5 étapes)
- [ ] Page de pricing publique + inscription self-service

**Critère de sortie Phase 1 :** 50 entreprises en beta fermée avec NPS > 40

---

### Phase 2 — Gestion de chantier (Mois 6–8)

**Objectif :** Couvrir le suivi terrain et la coordination

- [ ] Journal de chantier (entrées quotidiennes + météo auto)
- [ ] Gestion des plans (upload, visionneuse, annotations)
- [ ] Rapports journaliers PDF automatiques
- [ ] Planning Gantt chantier
- [ ] Tableau de bord chantiers (Kanban)
- [ ] Gestion des absences et congés
- [ ] GED chantier (documents, PPSPS, DOE)
- [ ] Relances automatiques factures impayées

**Critère de sortie Phase 2 :** 500 entreprises actives, churn < 3 %/mois

---

### Phase 3 — Pilotage Financier et Intégrations (Mois 9–11)

**Objectif :** Contrôle de gestion et connexion écosystème

- [ ] Tableaux de bord rentabilité (marge réelle vs prévisionnelle)
- [ ] Alertes marge sous seuil
- [ ] Intégrations comptables (Pennylane, Sage, EBP)
- [ ] Intégrations paie (SILAE, PayFit)
- [ ] API publique REST + documentation OpenAPI
- [ ] Webhooks configurables
- [ ] Gestion des achats et bons de commande fournisseurs
- [ ] Export DSN pour les pointages

**Critère de sortie Phase 3 :** 2 000 entreprises actives, MRR > 150 k€

---

### Phase 4 — IA et différenciation (Mois 12–18)

**Objectif :** Intelligence artificielle et fonctionnalités premium

- [ ] IA de suggestion de prix (basée sur historique interne + benchmarks marché)
- [ ] Dictée vocale avancée (transcription + mise en forme automatique)
- [ ] Détection d'anomalies de marge (alerte proactive)
- [ ] Prédiction des dépassements de budget (modèle ML sur historique chantiers)
- [ ] Recommandation d'affectation d'équipe (compétences + disponibilité + proximité géo)
- [ ] Assistant IA chat (répondre aux questions "quel est mon meilleur client ?")
- [ ] Visionneuse IFC 3D (modèles BIM)
- [ ] Application mobile — Interface Direction (parity web complète)

---

### Phase 5 — Scale et marketplace (Mois 18–24)

- [ ] Marketplace d'intégrations partenaires
- [ ] Module multi-société (groupes avec plusieurs entités juridiques)
- [ ] Portail sous-traitants (inviter les sous-traitants, partager plans et documents)
- [ ] Déploiement multilingue (EN, NL, ES en priorité)
- [ ] Conformité comptable Belgique, Suisse, Luxembourg

---

## 7. Stratégie d'accompagnement

### 7.1 Onboarding

**Semaine 0 — Inscription et setup**
- Formulaire d'inscription en 3 étapes (nom, email, corps de métier, taille entreprise)
- Email de bienvenue avec checklist "5 actions pour démarrer"
- Données de démonstration pré-chargées (entreprise fictive avec devis, chantiers, équipe)
- Vidéo de bienvenue personnalisée selon le corps de métier (électricien ≠ maçon)

**Semaine 1 — Activation**
- Checklist in-app gamifiée (barre de progression) :
  1. Créer votre premier devis
  2. Inviter un collaborateur
  3. Créer votre premier chantier
  4. Envoyer votre première facture
  5. Télécharger l'application mobile
- Appel de bienvenue proposé automatiquement à J+3 si < 3 actions complétées

**Semaine 2–4 — Adoption**
- Email d'astuces hebdomadaire (1 fonctionnalité par semaine, ton pratique)
- Webinaire de groupe mensuel (démo live, questions-réponses)
- Chat in-app avec l'équipe Customer Success (réponse < 4h en heures ouvrées)

### 7.2 Support client

**Principes**
- Support humain en premier (pas de bot qui tourne en rond)
- Équipe support composée d'anciens utilisateurs ou de personnes ayant une expérience BTP
- SLA publics et respectés contractuellement

**Canaux**
| Canal | Disponibilité | Temps de réponse cible |
|---|---|---|
| Chat in-app | Lun–Ven 8h–19h | < 2h (CHANTIER/ENTREPRISE) |
| Email | 24/7 | < 24h (STARTER), < 4h (autres) |
| Téléphone | Lun–Ven 9h–18h | < 1h (ENTREPRISE uniquement) |
| Base de connaissances | 24/7 | Self-service |

**Base de connaissances**
- Articles catégorisés par module et par persona
- Vidéos tutorielles courtes (< 3 min) pour chaque fonctionnalité clé
- Mises à jour synchronisées avec chaque déploiement (pas d'article périmé)

### 7.3 Formation

**Ressources incluses (tous plans)**
- Bibliothèque vidéo on-demand : 50+ tutoriels classés par niveau (débutant / avancé)
- Parcours de certification "BATISYNC Maîtrise" (attestation PDF en fin de parcours)
- Changelog vidéo : courte vidéo (< 2 min) à chaque mise à jour majeure

**Formation premium (ENTREPRISE ou en option)**
- Session d'onboarding personnalisée (2h via visio) : configuration de l'entreprise, import des données, formation des administrateurs
- Formation équipe terrain sur site (demi-journée) : prise en main de l'application mobile
- Atelier avancé trimestriel : pilotage financier, optimisation des marges

### 7.4 Politique de mise à jour et communication

- **Freeze de fonctionnalités** 2 semaines avant la clôture comptable (décembre, juin)
- **Communication pré-déploiement** : email J-7 pour les changements d'interface majeurs
- **Mode "ancien UX" temporaire** : possibilité de basculer sur l'ancienne interface pendant 30 jours après un redesign majeur
- **Comité utilisateurs** : groupe de 20 clients bêta-testeurs consultés avant chaque release majeure

### 7.5 Rétention et satisfaction

- **NPS** mesuré automatiquement à J+30, J+90, J+365 (in-app, 1 question)
- **Customer Success Review** semestrielle pour les comptes ENTREPRISE (analyse de l'usage, recommandations)
- **Programme de parrainage** : 1 mois offert pour chaque nouveau client parrainé
- **Communauté** : forum utilisateurs, partage de bibliothèques d'ouvrages entre entreprises du même corps de métier

---

## Annexe A — Matrice de risques

| Risque | Probabilité | Impact | Mitigation |
|---|---|---|---|
| Adoption terrain faible (ouvriers) | Élevée | Élevé | Interface ultra-simplifiée, formation sur site incluse en ENTREPRISE |
| Concurrence Vertuoza / Obat / Procore | Élevée | Moyen | Différenciation pricing transparent + offline mobile |
| Complexité technique offline sync | Moyenne | Élevé | WatermelonDB éprouvé, tests de régression automatisés |
| Churn en cas de bug post-mise à jour | Moyenne | Élevé | Feature flags, rollback auto, freeze pré-clôture |
| Dépendance API comptable tierce | Faible | Moyen | Abstraction layer, 2 partenaires par segment |

---

## Annexe B — Définition of Done

Une fonctionnalité est considérée "Done" quand :
1. Tests unitaires couvrent > 80 % du code nouveau
2. Tests d'intégration passent en CI
3. Tests de performance validés (objectif SLA respecté)
4. Documentation mise à jour dans la base de connaissances
5. Feature flag configuré pour déploiement progressif
6. Changelog rédigé
7. Revue design validée sur mobile et desktop
8. Revue sécurité validée (OWASP checklist)

---

*Document propriétaire — BATISYNC — Toute reproduction interdite sans autorisation écrite.*
