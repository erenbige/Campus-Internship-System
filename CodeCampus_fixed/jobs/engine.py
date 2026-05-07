class MatchEngine:
    """
    Singleton Pattern: Uygulama boyunca tek bir MatchEngine instance'ı kullanılır.
    Öğrenci becerileri ile iş ilanı gereksinimleri arasındaki uyum skorunu hesaplar.
    """
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MatchEngine, cls).__new__(cls)
        return cls._instance

    def calculate_score(self, student_skills: str, job_skills: str) -> float:
        """
        İki virgülle ayrılmış beceri string'ini karşılaştırır.
        Döner: 0.0 - 100.0 arasında eşleşme yüzdesi
        """
        if not job_skills or not student_skills:
            return 0.0

        job_skills_set = {
            skill.strip().lower()
            for skill in job_skills.split(',')
            if skill.strip()
        }
        student_skills_set = {
            skill.strip().lower()
            for skill in student_skills.split(',')
            if skill.strip()
        }

        if not job_skills_set:
            return 0.0

        matched_skills = job_skills_set.intersection(student_skills_set)
        score = (len(matched_skills) / len(job_skills_set)) * 100

        return round(score, 2)
